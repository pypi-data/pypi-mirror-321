""" stage dialog

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
import subprocess
import gi
import turtlevcs
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs import Notification, Question
from turtlevcs.dialogs.base import DialogBase

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio


class StageDialog(Notification, DialogBase):
    """ stage file dialog """
    app = None
    show_confirmation = True

    def __init__(self, path, parent=None, show_confirmation=True):
        Notification.__init__(self, "", title="Stage", parent=parent)
        DialogBase.__init__(self, path)

        self.show_confirmation = show_confirmation

        self.turtle.can_be_staged(path, raise_ex=True)

        checkbox = Gtk.CheckButton()
        checkbox.set_label("Show this dialog next time")
        settings = turtlevcs.get_settings()
        settings.bind("stage-show-information",
                           checkbox,
                           "active",
                           Gio.SettingsBindFlags.DEFAULT)
        self.set_extra_child(checkbox)
        self.set_body(
            "Staging will be done by meld.\n"
            "You can merge the chunks you want to stage to the right file.\n\n"
            "After meld is closed, you will be asked if you want to stage the file you saved.")

        self.connect("response", self._on_response)

    def _on_response(self, _dialog, _response):
        parent = self.get_parent()
        if parent is None:
            parent = self
        confirm = StageConfirmDialog(
            self.turtle, self.path, parent=parent, show_confirmation=self.show_confirmation)
        self.show_new_window(confirm)

class StageConfirmDialog(Question, DialogBase):
    """ confirm stage file dialog """
    file_path = None
    show_confirmation = True

    def __init__(self, turtle, path, parent=None, show_confirmation=True):
        Question.__init__(self, "Stage", callback=self._on_response, parent=parent)
        DialogBase.__init__(self, path, no_turtle=True)
        self.turtle = turtle

        self.show_confirmation = show_confirmation
        if isinstance(parent, StageDialog):
            self.show_confirmation = parent.show_confirmation

        _, new_or_deleted = self.turtle.can_be_staged(path, raise_ex=True)
        file = self.turtle.get_relative_file_path(path)

        if new_or_deleted:
            self.set_body(f"Do you want to stage '{file}'?")
        else:
            self.file_path = self.turtle.get_file_from_current_index(file, "STAGED")

            if self.file_path is not None:
                completed = subprocess.run(["meld", path, self.file_path.name], check=False)
                if completed.returncode != 0:
                    raise RuntimeError(f"failed to run process {completed.args[0]}")
                self.set_body(f"Do you want to stage '{file}' as saved?")
            else:
                raise IndexError("Index not valid")

    def _on_response(self, _dialog, response):
        if response == "yes":
            title = "Staged"
            message = "File has been staged."
            try:
                file = self.turtle.get_relative_file_path(self.path)
                self.turtle.stage_file_as_index(
                    self.file_path.name if self.file_path is not None else self.path,
                    file)
            except Exception as ex:
                title = "Failed"
                message = str(ex)

            if self.show_confirmation:
                notification = Notification(message, title=title, parent=self.get_transient_for())
                self.show_new_window(notification)

        try:
            parent = self.get_transient_for()
            parent.update()
        except Exception as _ex:
            pass

if __name__ == "__main__":
    SETTINGS = turtlevcs.get_settings()
    show_stage_info = SETTINGS.get_boolean("stage-show-information")

    TurtleApp(StageDialog if show_stage_info else StageConfirmDialog).run()
