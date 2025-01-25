""" turtle dbus service

This file is part of Turtle.

Turtle is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Turtle is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Turtle. If not, see <https://www.gnu.org/licenses/>. 
"""
import os
from pathlib import Path
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import pygit2
from turtlevcs import TURTLE_APP_ID, get_settings


TURTLE_OBJECT_PATH = "/Service"


class TurtleStatusChecker:
    """ turtle status checker """

    def __init__(self):
        pass

    def check_path(self, path):
        """ check status of path """
        status = pygit2.enums.FileStatus.CURRENT
        try:
            repo = pygit2.Repository(path)

            current_folder = repo.workdir
            new_repo_status = {}
            ignored_folders = []

            if os.path.isfile(path):
                file_path = path.removeprefix(repo.workdir)
                status = repo.status_file(file_path)
            else:
                if Path(path) == Path(repo.workdir):
                    new_repo_status = repo.status(ignored=True)
                else:
                    current_folder = str(Path(path).relative_to(repo.workdir)) + "/"
                    repo_status = repo.status(ignored=True)

                    for key, value in repo_status.items():
                        if value == pygit2.enums.FileStatus.IGNORED:
                            if current_folder.startswith(key):
                                # folder is ignored so we can return value already
                                return pygit2.enums.FileStatus.IGNORED
                            ignored_folders.append(key)
                        elif key.startswith(current_folder):
                            # item is in current folder
                            new_repo_status[key] = value

                status = self.__check_specific_folder(
                    path, repo, new_repo_status, current_folder, ignored_folders)
        except Exception as _ex:
            status = -1

        return status

    def __check_specific_folder(self, path, repo, repo_status, current_folder, ignored_folders):
        status = pygit2.enums.FileStatus.CURRENT

        if len(repo_status) > 0 or len(ignored_folders) > 0:
            if current_folder in repo_status:
                if repo_status[current_folder] == pygit2.enums.FileStatus.STATUS_IGNORED:
                    # folder is ignored, we can return at once
                    return pygit2.enums.FileStatus.STATUS_IGNORED

            status_modified = [
                pygit2.enums.FileStatus.CONFLICTED,
                pygit2.enums.FileStatus.WT_TYPECHANGE,
                pygit2.enums.FileStatus.WT_MODIFIED,
                # we treat index changed status as regular wt changed status inside a folder
                pygit2.enums.FileStatus.INDEX_TYPECHANGE,
                pygit2.enums.FileStatus.INDEX_MODIFIED,
            ]

            try:
                values = repo_status.values()
                if any(status in status_modified for status in values):
                    status = pygit2.enums.FileStatus.WT_MODIFIED
                else:
                    wt_new_files = 0
                    idx_new_files = 0
                    has_ignored_files = False
                    if pygit2.enums.FileStatus.WT_NEW in values:
                        wt_new_files = sum(i == pygit2.enums.FileStatus.WT_NEW for i in values)
                    if pygit2.enums.FileStatus.INDEX_NEW in values:
                        idx_new_files = sum(i == pygit2.enums.FileStatus.INDEX_NEW for i in values)

                    if wt_new_files > 0 or idx_new_files > 0 or len(ignored_folders) > 0:
                        files_in_folder = []
                        for current_path, subdirs, files in os.walk(path):
                            # do not consider ignored folders
                            current_path_relative = str(Path(current_path)
                                                        .relative_to(repo.workdir)) + "/"
                            if current_path_relative not in ignored_folders and not any(
                                current_path_relative
                                .endswith(ignored_folder) for ignored_folder in ignored_folders):
                                for file in files:
                                    full_file = current_path_relative + file
                                    if full_file not in ignored_folders:
                                        files_in_folder.append(current_path_relative + file)
                            else:
                                # ignore all subdirectories if current_path is ignored
                                subdirs.clear()
                                has_ignored_files = True

                        # only set new / ignored status if there are no other files in the folder
                        if wt_new_files + idx_new_files == len(files_in_folder):
                            if idx_new_files > 0:
                                status = pygit2.enums.FileStatus.INDEX_NEW
                            elif wt_new_files > 0:
                                status = pygit2.enums.FileStatus.WT_NEW
                            elif has_ignored_files:
                                status = pygit2.enums.FileStatus.IGNORED
            except Exception as _ex:
                pass
        else:
            content = os.listdir(path)
            if len(content) == 0:
                status = pygit2.enums.FileStatus.INDEX_NEW

        return status


class TurtleService(dbus.service.Object):
    """ turtle dbus service """

    checker = None

    def __init__(self, connection, object_path):
        dbus.service.Object.__init__(self, connection, object_path)
        self.checker = TurtleStatusChecker()

    @dbus.service.method(TURTLE_APP_ID, in_signature="xsb", out_signature="xibbbb")
    def status_for_path(self, key, path, is_repo_base):
        """ calculate git status for path """
        status = -1
        show_emblems = False
        show_turtle_emblem = False
        show_status_emblem = False
        enable_everywhere = False
        try:
            settings = get_settings()
            show_emblems = settings.get_boolean("show-emblems")
            show_turtle_emblem = settings.get_boolean("show-turtle-emblem")
            show_status_emblem = settings.get_boolean("show-status-emblem")
            enable_everywhere = settings.get_boolean("enable-everywhere")

            if show_emblems and show_status_emblem or not is_repo_base:
                status = self.checker.check_path(path)

            return key, status, show_emblems, show_turtle_emblem, show_status_emblem, enable_everywhere
        except Exception as _ex:
            print(f"exception {str(_ex)}")
            return -1, status, show_emblems, show_turtle_emblem, show_status_emblem, enable_everywhere

    @dbus.service.method(TURTLE_APP_ID, out_signature="i")
    def get_pid(self):
        """ retrieve the pid of this process """
        return os.getpid()


class TurtleServiceConnector:
    """ turtle dbus service connector """

    session_bus = None
    turtle = None

    def get_pid(self):
        """ get pid of current turtle service process """
        self._get_bus()

        return self.turtle.get_pid(dbus_interface=TURTLE_APP_ID)

    def _get_bus(self):
        if self.session_bus is None:
            DBusGMainLoop(set_as_default=True)
            self.session_bus = dbus.SessionBus()
        if self.turtle is None:
            self.turtle = self.session_bus.get_object(TURTLE_APP_ID, TURTLE_OBJECT_PATH)

    def _status_for_path_from_service(
            self, key, path, is_repo_base,
            reply_handler, error_handler):
        try:
            self._get_bus()

            self.turtle.status_for_path(
                key,
                path,
                is_repo_base,
                dbus_interface=TURTLE_APP_ID,
                reply_handler=reply_handler,
                error_handler=error_handler)
        except dbus.DBusException as ex:
            print(f"dbus communication failed: {str(ex)}")
