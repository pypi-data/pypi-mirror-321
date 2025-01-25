""" init dialog

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
import gi
import turtlevcs.turtle
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs import Notification

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gio


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/init.ui")
class InitWindow(Adw.ApplicationWindow, DialogBase):
    """ init dialog """
    __gtype_name__ = "InitWindow"

    init_button = Gtk.Template.Child()
    directory_entry = Gtk.Template.Child()
    bare_checkbutton = Gtk.Template.Child()

    path = ""
    open_dialog = None

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path, no_turtle=True)

        #self._set_title_branch()
        self.path = path
        self.directory_entry.set_text(path)

        self.__refresh()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__refresh()

    def __refresh(self):
        self.init_button.set_sensitive(False)

        self.init_button.set_sensitive(True)

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        directory = self.directory_entry.get_text()
        bare = self.bare_checkbutton.get_active()

        message = f"Created repo at {directory}"
        title = "Init Done"

        try:
            turtlevcs.turtle.init(directory, bare)
        except Exception as ex:
            title = "Init Failed"
            message = str(ex)

        notification = Notification(message, title=title, parent=self)

        notification.connect("response", self._on_close_by_progress)
        notification.set_visible(True)

    @Gtk.Template.Callback()
    def _directory_entry_changed_handler(self, widget):
        pass

    @Gtk.Template.Callback()
    def _directory_entry_button_handler(self, _widget):
        directory = self.directory_entry.get_text()
        if not self.open_dialog:
            self.open_dialog = Gtk.FileChooserNative.new(
                title="Choose a directory",
                parent=self, action=Gtk.FileChooserAction.SELECT_FOLDER)
            self.open_dialog.connect("response", self._open_directory_callback)
        if len(directory) > 0 and os.path.exists(directory):
            self.open_dialog.set_current_folder(Gio.File.new_for_path(directory))
        else:
            self.open_dialog.set_current_folder(Gio.File.new_for_path(self.path))
        self.open_dialog.show()

    def _open_directory_callback(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            path = dialog.get_file().get_path()
            if os.path.exists(path):
                self.directory_entry.set_text(path)


if __name__ == "__main__":
    TurtleApp(InitWindow).run()
