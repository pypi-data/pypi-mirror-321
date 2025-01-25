""" about dialog

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
import turtlevcs
from turtlevcs.turtle_app import TurtleApp
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


class About():
    """ about dialog """
    window = None

    def __init__(self, _path=None):
        self.window = Adw.AboutWindow()

        authors = ["Philipp Unger"]
        artists = ["Brage Fuglseth"]

        self.window.set_application_name("Turtle")
        self.window.set_version(turtlevcs.get_full_version())
        self.window.set_developers(authors)
        self.window.set_artists(artists)
        self.window.set_license_type(Gtk.License.GPL_3_0)
        self.window.set_application_icon(turtlevcs.TURTLE_APP_ID)
        self.window.set_website("https://gitlab.gnome.org/philippun1/turtle")
        self.window.set_issue_url("https://gitlab.gnome.org/philippun1/turtle/-/issues")

if __name__ == "__main__":
    TurtleApp(About).run()
