""" clone dialog

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
import pathlib
import gi
import turtlevcs.turtle
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gdk, Gio


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/clone.ui")
class CloneWindow(Adw.ApplicationWindow, DialogBase):
    """ clone dialog """
    __gtype_name__ = "CloneWindow"

    clone_button = Gtk.Template.Child()
    url_entry = Gtk.Template.Child()
    directory_entry = Gtk.Template.Child()
    recursive = Gtk.Template.Child()
    bare = Gtk.Template.Child()

    open_dialog = None

    url = None
    directory = None

    path = None


    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path, no_turtle=True)
        self.path = path

        clipboard = Gdk.Display().get_default().get_clipboard()
        clipboard.read_text_async(cancellable=None, callback=self._read_clipboard)

        self.__update()

    def _read_clipboard(self, clipboard, result):
        try:
            data = clipboard.read_text_finish(result)
            if data.startswith("git@") or data.startswith("https://"):
                self.url_entry.set_text(data)
        except Exception:
            pass

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    def __update(self):
        self.clone_button.set_sensitive(False)

        valid = self.__get_entry_texts()

        self.clone_button.set_sensitive(valid)

    def __get_entry_texts(self):
        self.url = self.url_entry.get_text()
        self.directory = self.directory_entry.get_text()

        return len(self.url) > 0 and len(self.directory) > 0

    def __clone(self):
        self._show_progress_window("Cloning", self._do_clone)

    def _do_clone(self):
        recursive = self.recursive.get_active()
        bare = self.bare.get_active()
        new_repo = None
        message = ""
        try:
            new_repo = turtlevcs.turtle.clone(
                self.url,
                self.directory,
                recursive,
                bare,
                self._update_progress_message)
        except Exception as ex:
            message = str(ex)

        if new_repo:
            summary = "Cloned"
            message = "Successfully cloned branch."
        else:
            summary = "Cloning Failed"

        self._set_progress_message(summary, details=message)

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        self.__clone()

    @Gtk.Template.Callback()
    def _url_changed(self, _widget):
        url = self.url_entry.get_text()
        directory = self.directory_entry.get_text()
        if len(directory) == 0 and url.startswith("git@") or url.startswith("https://"):
            folder = url.split("/")[-1].removesuffix(".git")
            folder_path = pathlib.Path(self.path) / folder
            self.directory_entry.set_text(str(folder_path))

        self.__update()

    @Gtk.Template.Callback()
    def _directory_changed(self, _widget):
        self.__update()

    @Gtk.Template.Callback()
    def _directory_entry_button_handler(self, _widget):
        self.__get_entry_texts()
        if not self.open_dialog:
            self.open_dialog = Gtk.FileChooserNative.new(
                title="Choose a directory",
                parent=self, action=Gtk.FileChooserAction.SELECT_FOLDER)
            self.open_dialog.connect("response", self._open_directory_callback)
        if len(self.directory) > 0 and os.path.exists(self.directory):
            self.open_dialog.set_current_folder(Gio.File.new_for_path(self.directory))
        else:
            self.open_dialog.set_current_folder(Gio.File.new_for_path(self.path))
        self.open_dialog.show()

    def _open_directory_callback(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            path = dialog.get_file().get_path()
            if os.path.exists(path):
                self.directory_entry.set_text(path)


if __name__ == "__main__":
    TurtleApp(CloneWindow).run()
