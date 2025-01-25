""" diff file dialog

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
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs import Subprocess
from turtlevcs.dialogs.base import DialogBase


class DiffFile(Subprocess, DialogBase):
    """ diff file """
    def __init__(self, path):
        Subprocess.__init__(self, process_args=None, start_automatically=False)
        DialogBase.__init__(self, path)

        if not os.path.isfile(path):
            raise AttributeError("diff_file only works with files")

        relative_path = self.turtle.get_relative_file_path(path)
        temp2 = self.turtle.get_file_from_index(relative_path)
        self.temp_file2 = temp2
        self.process_args = ["meld", temp2.name, path]

        self.start()

if __name__ == "__main__":
    TurtleApp(DiffFile).run()
