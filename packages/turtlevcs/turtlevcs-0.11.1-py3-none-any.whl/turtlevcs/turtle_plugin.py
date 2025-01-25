""" turtle plugin base

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
import pygit2
from gi.repository import Gio
import turtlevcs
from turtlevcs.service import TurtleServiceConnector


class TurtlePlugin(TurtleServiceConnector):
    """ turtle plugin """

    repo = None

    menu_item_creator = None
    menu_creator = None

    handles = {}

    # store current settings
    show_emblems = False
    show_turtle_emblem = False
    show_status_emblem = False
    enable_everywhere = False

    # will be used by pytest
    finished_callback = None

    def __init__(self, menu_item_creator, menu_creator):
        self.menu_item_creator = menu_item_creator
        self.menu_creator = menu_creator

        try:
            self._get_bus()
        except Exception as ex:
            print(f"cannot connect to dbus service: {str(ex)}")

    def _open_turtle(self, module, path):
        os.system(f"turtle_cli '{module}' '{path}' &")

    def _menu_activate_cb(self, menu, module, path):
        self._open_turtle(module, path)

    def __create_menu_entries(self, path, additional, is_file=False, file_list=[]):
        commit = self.menu_item_creator(
            name=self.__create_menu_item_name("Commit", additional),
            label="Commit")
        if len(file_list) > 0:
            path = ",".join(f.get_location().get_path() for f in file_list)
        commit.connect("activate", self._menu_activate_cb, "commit", path)

        sync = self.menu_item_creator(
            name=self.__create_menu_item_name("Sync", additional),
            label="Sync")
        sync.connect("activate", self._menu_activate_cb, "sync", path)

        entries = [commit, sync]
        if is_file:
            status = self.repo.status()
            file = path.removeprefix(self.repo.workdir)
            if file in status:
                if status[file] & pygit2.enums.FileStatus.WT_MODIFIED > 0:
                    diff_file = self.menu_item_creator(
                        name=self.__create_menu_item_name("Diff", additional),
                        label="Diff")
                    diff_file.connect("activate", self._menu_activate_cb, "diff_file", path)

                    entries.append(diff_file)

        return entries

    def __create_submenu(self, path, additional, is_file=False, non_repo=False):
        turtle_menu = self.menu_item_creator(
            name=self.__create_menu_item_name("Turtle", additional),
            label="Turtle")
        submenu = self.menu_creator()
        try:
            turtle_menu.set_submenu(submenu)
        except Exception as _ex:
            # fallback to set_menu mode for thunar
            turtle_menu.set_menu(submenu)

        if non_repo:
            init = self.menu_item_creator(
                name=self.__create_menu_item_name("Init", additional),
                label="Init")
            init.connect("activate", self._menu_activate_cb, "init", path)
            submenu.append_item(init)

            clone = self.menu_item_creator(
                name=self.__create_menu_item_name("Clone", additional),
                label="Clone")
            clone.connect("activate", self._menu_activate_cb, "clone", path)
            submenu.append_item(clone)
        else:
            diff = self.menu_item_creator(
                name=self.__create_menu_item_name("Diff", additional),
                label="Diff")
            diff.connect("activate", self._menu_activate_cb, "diff", path)
            submenu.append_item(diff)

            log = self.menu_item_creator(
                name=self.__create_menu_item_name("Log", additional),
                label="Log")
            log.connect("activate", self._menu_activate_cb, "log", path)
            submenu.append_item(log)

            add = self.menu_item_creator(
                name=self.__create_menu_item_name("Add", additional),
                label="Add")
            add.connect("activate", self._menu_activate_cb, "add", path)
            submenu.append_item(add)

            if is_file:
                # for files we check if we can actually revert or (un)stage
                status = self.repo.status()
                file = path.removeprefix(self.repo.workdir)
                if file in status:
                    has_wt_status, _ = turtlevcs.has_worktree_status(status[file])
                    has_index_status, _ = turtlevcs.has_index_status(status[file])

                    if has_wt_status:
                        revert = self.menu_item_creator(
                            name=self.__create_menu_item_name("Revert", additional),
                            label="Revert")
                        revert.connect("activate", self._menu_activate_cb, "revert", path)
                        submenu.append_item(revert)

                        stage = self.menu_item_creator(
                            name=self.__create_menu_item_name("Stage", additional),
                            label="Stage")
                        stage.connect("activate", self._menu_activate_cb, "stage", path)
                        submenu.append_item(stage)

                    if has_index_status:
                        unstage = self.menu_item_creator(
                            name=self.__create_menu_item_name("Unstage", additional),
                            label="Unstage")
                        unstage.connect("activate", self._menu_activate_cb, "unstage", path)
                        submenu.append_item(unstage)
            else:
                # always show revert for non files
                revert = self.menu_item_creator(
                    name=self.__create_menu_item_name("Revert", additional),
                    label="Revert")
                revert.connect("activate", self._menu_activate_cb, "revert", path)
                submenu.append_item(revert)

            clean = self.menu_item_creator(
                name=self.__create_menu_item_name("Clean", additional),
                label="Clean")
            clean.connect("activate", self._menu_activate_cb, "clean", path)
            submenu.append_item(clean)

            push = self.menu_item_creator(
                name=self.__create_menu_item_name("Push", additional),
                label="Push")
            push.connect("activate", self._menu_activate_cb, "push", path)
            submenu.append_item(push)

            pull = self.menu_item_creator(
                name=self.__create_menu_item_name("Pull", additional),
                label="Pull")
            pull.connect("activate", self._menu_activate_cb, "pull", path)
            submenu.append_item(pull)

            merge = self.menu_item_creator(
                name=self.__create_menu_item_name("Merge", additional),
                label="Merge")
            merge.connect("activate", self._menu_activate_cb, "merge", path)
            submenu.append_item(merge)

            checkout = self.menu_item_creator(
                name=self.__create_menu_item_name("Checkout", additional),
                label="Checkout")
            checkout.connect("activate", self._menu_activate_cb, "checkout", path)
            submenu.append_item(checkout)

            create_branch = self.menu_item_creator(
                name=self.__create_menu_item_name("CreateBranch", additional),
                label="Create Branch")
            create_branch.connect("activate", self._menu_activate_cb, "create_branch", path)
            submenu.append_item(create_branch)

            create_tag = self.menu_item_creator(
                name=self.__create_menu_item_name("CreateTag", additional),
                label="Create Tag")
            create_tag.connect("activate", self._menu_activate_cb, "create_tag", path)
            submenu.append_item(create_tag)

            resolve = self.menu_item_creator(
                name=self.__create_menu_item_name("Resolve", additional),
                label="Resolve")
            resolve.connect("activate", self._menu_activate_cb, "resolve", path)
            submenu.append_item(resolve)

            reset = self.menu_item_creator(
                name=self.__create_menu_item_name("Reset", additional),
                label="Reset")
            reset.connect("activate", self._menu_activate_cb, "reset", path)
            submenu.append_item(reset)

            references = self.menu_item_creator(
                name=self.__create_menu_item_name("References", additional),
                label="References")
            references.connect("activate", self._menu_activate_cb, "references", path)
            submenu.append_item(references)

            remotes = self.menu_item_creator(
                name=self.__create_menu_item_name("Remotes", additional),
                label="Remotes")
            remotes.connect("activate", self._menu_activate_cb, "remotes", path)
            submenu.append_item(remotes)

            submodules = self.menu_item_creator(
                name=self.__create_menu_item_name("Submodules", additional),
                label="Submodules")
            submodules.connect("activate", self._menu_activate_cb, "submodules", path)
            submenu.append_item(submodules)

        settings = self.menu_item_creator(
            name=self.__create_menu_item_name("Settings", additional),
            label="Settings")
        settings.connect("activate", self._menu_activate_cb, "settings", path)
        submenu.append_item(settings)

        about = self.menu_item_creator(
            name=self.__create_menu_item_name("About", additional),
            label="About")
        about.connect("activate", self._menu_activate_cb, "about", path)
        submenu.append_item(about)

        return turtle_menu

    def create_menus(self, files, additional):
        """ create menu entries """
        menu_items = []
        file = files[0]
        try:
            path = file.get_location().get_path()
            uri = file.get_uri()
            # only use local files for now
            if uri.startswith("file://"):
                try:
                    is_file = file.get_file_type() == Gio.FileType.REGULAR
                except Exception as _ex:
                    # TODO fallback for thunar
                    is_file = not file.is_directory()
                self.repo = pygit2.Repository(path)
                menu_entries = self.__create_menu_entries(path, additional, is_file, files)
                submenu = self.__create_submenu(path, additional, is_file)
                menu_items = menu_entries + [submenu]
        except Exception as _ex:
            if self.enable_everywhere:
                submenu = self.__create_submenu(path, additional, non_repo=True)
                menu_items = [submenu]

        return menu_items

    def update_file_info(self, file):
        """ update_file_info from Nautilus.InfoProvider """

        try:
            uri = file.get_uri()
            # only use local files for now
            if uri.startswith("file://"):
                path = file.get_location().get_path()

                try:
                    is_repo_base = False
                    if os.path.exists(path + "/.git"):
                        is_repo_base = True
                        if not self.show_status_emblem and not self.show_turtle_emblem:
                            return

                    key = id(file)
                    self.handles[key] = (file, is_repo_base)

                    self._status_for_path_from_service(
                        key,
                        path,
                        is_repo_base,
                        self._check_folder_async_finished,
                        self._check_folder_async_error)
                except Exception as _ex:
                    pass
        except Exception as _ex:
            pass

    def _check_folder_async_finished(
            self, key, status,
            show_emblems, show_turtle_emblem,
            show_status_emblem, enable_everywhere):
        # store settings locally to avoid unnecessary dbus calls
        # (which might end up as bottle neck)
        self.show_emblems = show_emblems
        self.show_turtle_emblem = show_turtle_emblem
        self.show_status_emblem = show_status_emblem
        self.enable_everywhere = enable_everywhere

        try:
            (file, is_repo_base) = self.handles.pop(key, None)

            if show_emblems and file is not None:
                if self.show_turtle_emblem and is_repo_base:
                    file.add_emblem("de.philippun1.turtle-symbolic")
                if self.show_status_emblem or not is_repo_base:
                    status = int(status)
                    if status > -1:
                        self._set_emblem_for_status(file, status)

            if self.finished_callback:
                self.finished_callback()
        except Exception as _ex:
            pass

    def _check_folder_async_error(self, error):
        print(f"check folder async error: {error}")

    def _set_emblem_for_status(self, file, status):
        try:
            emblem = turtlevcs.status_icon_map[status]
        except Exception as _ex:
            # special case if file has WT and INDEX status
            emblem = "emblem-important"

        file.add_emblem(emblem)

    def __create_menu_item_name(self, name, additional=""):
        item_name = "TurtleMenuProvider::"
        if len(additional) > 0:
            item_name += additional + "::"

        item_name += name

        return item_name
