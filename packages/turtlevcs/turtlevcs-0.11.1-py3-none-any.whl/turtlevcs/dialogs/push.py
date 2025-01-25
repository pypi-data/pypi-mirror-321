""" push dialog

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
from turtlevcs.dialogs.base import DialogBase, PushBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/push.ui")
class PushWindow(Adw.ApplicationWindow, DialogBase, PushBase):
    """ push window """
    __gtype_name__ = "PushWindow"

    push_button = Gtk.Template.Child()
    branch = Gtk.Template.Child()
    upstream = Gtk.Template.Child()

    branch_model = Gtk.Template.Child()
    upstream_model = Gtk.Template.Child()
    scrolled_window = Gtk.Template.Child()

    is_updating = False

    branch_name = None
    remote_name = None
    push_table = None

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        PushBase.__init__(self)

        self.scrolled_window.set_child(self.push_table)

        self._set_title_repo()

        self.__refresh()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__refresh()

    def __refresh(self):
        self.is_updating = True
        self.push_button.set_sensitive(False)

        self._fill_branch_data(prefer_origin=True)

        branch_name, remote_name = self._get_selected_branch_and_upstream_names()
        can_push = self.push_table.update_commits(branch_name, remote_name)
        self.push_button.set_sensitive(can_push)

        self.is_updating = False

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        self._push()

    @Gtk.Template.Callback()
    def _refresh_clicked(self, widget):
        self.__refresh()

    @Gtk.Template.Callback()
    def _branch_changed_handler(self, _widget, _property):
        self._branch_or_upstream_changed()

    @Gtk.Template.Callback()
    def _upstream_changed_handler(self, _widget, _property):
        self._branch_or_upstream_changed()


if __name__ == "__main__":
    TurtleApp(PushWindow).run()
