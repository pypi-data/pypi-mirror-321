""" pull dialog

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
from turtlevcs.turtle import PullAction
from turtlevcs.dialogs.base import DialogBase, PullBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/pull.ui")
class PullWindow(Adw.ApplicationWindow, DialogBase, PullBase):
    """ pull dialog """
    __gtype_name__ = "PullWindow"

    pull_button = Gtk.Template.Child()

    fetch_only = Gtk.Template.Child()
    fetch_and_merge = Gtk.Template.Child()
    fetch_and_rebase = Gtk.Template.Child()

    first_refresh = True
    is_updating = False
    can_push = False

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        PullBase.__init__(self)

        self._set_title_branch()

        self.__refresh()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__refresh()

    def __refresh(self):
        self.pull_button.set_sensitive(False)

        self.pull_button.set_sensitive(True)

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        if self.fetch_only.get_active():
            pull_action = PullAction.FETCH_ONLY
        elif self.fetch_and_merge.get_active():
            pull_action = PullAction.FETCH_AND_MERGE
        elif self.fetch_and_rebase.get_active():
            pull_action = PullAction.FETCH_AND_REBASE
        self._pull(pull_action=pull_action)


if __name__ == "__main__":
    TurtleApp(PullWindow).run()
