""" revert dialog

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
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs import Notification, Question
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs.add import AddWindow



class RevertFileDialog(Question, DialogBase):
    """ revert file dialog """
    def __init__(self, path):
        Question.__init__(self, "Revert", self._on_response)
        DialogBase.__init__(self, path)

        file = self.turtle.get_relative_file_path(path)

        _, wt_new = self.turtle.can_be_reverted(file, raise_ex=True)
        self.set_body(f"Do you want to {'delete' if wt_new else 'revert'} '{file}'?")

    def _on_response(self, _widget, response):
        if response == "yes":
            try:
                file = self.turtle.get_relative_file_path(self.path)
                self.turtle.revert(file)

                title = "Reverted"
                message = f"File '{file}' reverted"
            except Exception as ex:
                title = "Revert Failed"
                message = f"Revert of file '{file}' has failed: {str(ex)}"

            notification = Notification(message, title)
            self.show_new_window(notification)


if __name__ == "__main__":
    args = sys.argv
    IS_FILE = False

    if len(args) > 1:
        _path = args[1]
        if os.path.isfile(_path):
            IS_FILE = True

    # we can just reuse the AddWindow, which also supports reverting
    if IS_FILE:
        TurtleApp(RevertFileDialog).run()
    else:
        TurtleApp(AddWindow, parameter=True).run()
