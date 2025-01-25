""" clean dialog

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
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs import Notification

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/clean.ui")
class CleanWindow(Adw.ApplicationWindow, DialogBase):
    """ clean dialog """
    __gtype_name__ = "CleanWindow"

    clean_button = Gtk.Template.Child()
    clean_type_row = Gtk.Template.Child()
    directories_switch = Gtk.Template.Child()
    textview = Gtk.Template.Child()

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)

        self._set_title_repo()

        self.__update()

    def _on_refresh_clicked(self):
        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    @Gtk.Template.Callback()
    def _clean_clicked(self, _widget):
        self._show_progress_window("Cleaning", None)
        cleaned_files = self.__clean(dry_run=False)
        self._set_progress_message(f"{len(cleaned_files)} items removed", "Cleaned")

    @Gtk.Template.Callback()
    def _type_changed_handler(self, _widget, _property):
        self.__update()

    @Gtk.Template.Callback()
    def _directories_changed_handler(self, _widget, _state):
        self.__update()

    def __clean(self, dry_run):
        clean_type = self.clean_type_row.get_selected_item().get_string()
        non_ignored = True
        ignored = True
        if clean_type == "Non-ignored files":
            non_ignored = True
            ignored = False
        elif clean_type == "Only ignored files":
            non_ignored = False
            ignored = True

        directories = self.directories_switch.get_active()
        cleaned_files = self.turtle.clean(non_ignored, ignored, directories, dry_run)

        return cleaned_files

    def __update(self):
        self.clean_button.set_sensitive(False)

        cleaned_files = self.__clean(dry_run=True)

        text = "\n".join(cleaned_files)
        buf = self.textview.get_buffer()
        buf.set_text(text)

        self.clean_button.set_sensitive(True)


if __name__ == "__main__":
    TurtleApp(CleanWindow).run()
