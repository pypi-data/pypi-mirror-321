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
import gi
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs import Notification, Question
from turtlevcs.dialogs.base import DialogBase


class UnstageConfirmDialog(Question, DialogBase):
    """ unstage dialog """
    file_path = None
    show_confirmation = True

    def __init__(self, path, parent=None, show_confirmation=True):
        Question.__init__(self, "Unstage", callback=self._on_response, parent=parent)
        DialogBase.__init__(self, path)

        self.show_confirmation = show_confirmation

        self.turtle.can_be_unstaged(path, raise_ex=True)
        file = self.turtle.get_relative_file_path(path)

        self.set_body(f"Do you want to unstage '{file}'?")

    def _on_response(self, _dialog, response):
        if response == "yes":
            title = "Unstaged"
            message = "File has been unstaged."
            try:
                file = self.turtle.get_relative_file_path(self.path)
                self.turtle.unstage(file)
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
    TurtleApp(UnstageConfirmDialog).run()
