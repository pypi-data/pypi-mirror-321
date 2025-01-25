""" add dialog

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
import sys
import gi
import pygit2
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs import Notification
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs.commit_table import CommitTable

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


class AddFileDialog(Notification, DialogBase):
    """ add file dialog """
    def __init__(self, path):
        Notification.__init__(self, "", title="Added")
        DialogBase.__init__(self, path)

        try:
            file = self.turtle.get_relative_file_path(path)
            self.turtle.add([file], [])

            self.set_body(f"File '{file}' added")
        except Exception as ex:
            self.set_title("Add Failed")
            self.set_body(f"Adding of file '{file}' has failed: {str(ex)}")



@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/add.ui")
class AddWindow(Adw.ApplicationWindow, DialogBase):
    """ add dialog """
    __gtype_name__ = "AddWindow"

    add_button = Gtk.Template.Child()
    scolled_window = Gtk.Template.Child()

    listview = None
    revert_instead_of_add = False

    def __init__(self, path, revert_instead_of_add=False):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)

        self.revert_instead_of_add = revert_instead_of_add

        if self.revert_instead_of_add:
            self.add_button.set_label("Revert")

        self.listview = CommitTable(self.turtle, parent_window=self)
        self.scolled_window.set_child(self.listview)

        self._set_title_repo()

        self.__update()

    def update(self):
        """ public update function to be called from stage dialog """
        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    def __update(self):
        self.add_button.set_sensitive(False)

        status, _ = self.turtle.get_commit_info(
            not self.revert_instead_of_add,
            False,
            False)

        can_add = self.listview.update_model_with_status(status, hide_staged=True)

        self.add_button.set_sensitive(can_add)

    def __add(self, response=True):
        if response:
            self._show_progress_window(
                "Reverting" if self.revert_instead_of_add else "Adding", self._do_add)

    def _do_add(self):
        total = 0
        files = []
        deleted_files = []
        error = None

        count = self.listview.model.get_n_items()
        i = 0
        while i < count:
            item = self.listview.model.get_item(i)
            i += 1
            if item.selected:
                if self.revert_instead_of_add:
                    if self.turtle.can_be_reverted(item.path):
                        self.turtle.revert(item.path)
                        total += 1
                else:
                    if item.status in [
                        pygit2.enums.FileStatus.INDEX_DELETED, pygit2.enums.FileStatus.WT_DELETED]:
                        deleted_files.append(item.path)
                    else:
                        files.append(item.path)

        if not self.revert_instead_of_add:
            total = self.turtle.add(files, deleted_files)

        if total > 0:
            summary = "Reverted" if self.revert_instead_of_add else "Added"
            error = f"{total} file(s) {'reverted' if self.revert_instead_of_add else 'added'}"
        elif total < 0:
            summary = f"{'Revert' if self.revert_instead_of_add else 'Add'} failed"
        else:
            summary = f"No files {'reverted' if self.revert_instead_of_add else 'added'}"

        self._set_progress_message(summary, error)

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        self.__add()

    @Gtk.Template.Callback()
    def _refresh_clicked(self, widget):
        self.__update()


if __name__ == "__main__":
    args = sys.argv
    IS_FILE = False

    if len(args) > 1:
        PATH = args[1]
        if os.path.isfile(PATH):
            IS_FILE = True

    TurtleApp(AddFileDialog if IS_FILE else AddWindow).run()
