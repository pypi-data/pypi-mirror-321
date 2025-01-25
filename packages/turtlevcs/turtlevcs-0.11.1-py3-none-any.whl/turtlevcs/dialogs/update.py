""" update dialog

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
from turtlevcs.turtle import PullAction
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase, PullBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/update.ui")
class UpdateWindow(Adw.ApplicationWindow, DialogBase, PullBase):
    """ update window """
    __gtype_name__ = "UpdateWindow"

    update_button = Gtk.Template.Child()
    branch = Gtk.Template.Child()
    upstream = Gtk.Template.Child()
    fetch = Gtk.Template.Child()
    fetch_and_merge = Gtk.Template.Child()
    fetch_and_rebase = Gtk.Template.Child()

    branch_model = Gtk.Template.Child()
    upstream_model = Gtk.Template.Child()

    is_updating = False

    branch_name = None
    remote_name = None

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        PullBase.__init__(self)

        self._set_title_repo()

        self.__refresh()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__refresh()

    def __refresh(self):
        self.is_updating = True
        self.update_button.set_sensitive(False)

        self._fill_branch_data()

        self.__refresh_on_change()
        self.is_updating = False

    def __refresh_on_change(self):
        self.update_button.set_sensitive(False)

        branch_name, remote_name = self._get_selected_branch_and_upstream_names()
        upstream_available = self.turtle.get_branch_upstream(branch_name)

        self.update_button.set_sensitive(branch_name and remote_name and upstream_available)

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        if self.fetch.get_active():
            pull_action = PullAction.FETCH_ONLY
        elif self.fetch_and_merge.get_active():
            pull_action = PullAction.FETCH_AND_MERGE
        elif self.fetch_and_rebase.get_active():
            pull_action = PullAction.FETCH_AND_REBASE
        self._pull(pull_action=pull_action)

    @Gtk.Template.Callback()
    def _refresh_clicked(self, widget):
        self.__refresh()

    @Gtk.Template.Callback()
    def _branch_changed_handler(self, _widget, _property):
        if not self.is_updating:
            self.__refresh_on_change()

    @Gtk.Template.Callback()
    def _upstream_changed_handler(self, _widget, _property):
        if not self.is_updating:
            self.__refresh_on_change()


if __name__ == "__main__":
    TurtleApp(UpdateWindow).run()
