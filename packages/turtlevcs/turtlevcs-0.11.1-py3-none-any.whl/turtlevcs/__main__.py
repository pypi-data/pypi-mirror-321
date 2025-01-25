""" turtlevcs main entry point

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
import sys
import turtlevcs


if __name__ == "__main__":
    parser = turtlevcs.create_parser("python -m turtlevcs", "python module")
    arguments = parser.parse_args(sys.argv[1:])

    turtlevcs.launch_dialog(arguments.module, sys.argv[2:])
