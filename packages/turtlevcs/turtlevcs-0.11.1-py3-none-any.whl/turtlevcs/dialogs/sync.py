""" sync dialog

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
from turtlevcs.dialogs.base import DialogBase, PushBase, PullBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gio


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/sync.ui")
class SyncWindow(Adw.ApplicationWindow, DialogBase, PushBase, PullBase):
    """ sync dialog """
    __gtype_name__ = "SyncWindow"

    pull_button = Gtk.Template.Child()
    push_button = Gtk.Template.Child()
    settings = Gtk.Template.Child()

    branch = Gtk.Template.Child()
    upstream = Gtk.Template.Child()

    branch_model = Gtk.Template.Child()
    upstream_model = Gtk.Template.Child()
    scrolled_window = Gtk.Template.Child()

    action_push = None

    first_refresh = True
    is_updating = False

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        PushBase.__init__(self)
        PullBase.__init__(self)

        self.scrolled_window.set_child(self.push_table)

        self._set_title_repo()

        self.action_pull = Gio.SimpleAction.new("action-pull", None)
        self.action_pull.connect("activate", self._button_action_handler)
        self.add_action(self.action_pull)
        self.action_fetch = Gio.SimpleAction.new("action-fetch", None)
        self.action_fetch.connect("activate", self._button_action_handler)
        self.add_action(self.action_fetch)
        # self.action_rebase = Gio.SimpleAction.new("action-fetch-and-rebase", None)
        # self.action_rebase.connect("activate", self._button_action_handler)
        # self.add_action(self.action_rebase)

        self.__refresh()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__refresh()

    def _button_action_handler(self, action, _data):
        if action.get_name() == "action-pull":
            self.pull_button.set_label("Pull")
        elif action.get_name() == "action-fetch":
            self.pull_button.set_label("Fetch")

        self.__refresh()

    def __refresh(self):
        self.pull_button.set_sensitive(False)
        self.push_button.set_sensitive(False)

        self._fill_branch_data(prefer_origin=True)

        branch_name, remote_name = self._get_selected_branch_and_upstream_names()
        can_push = self.push_table.update_commits(branch_name, remote_name)

        self.pull_button.set_sensitive(True)
        self.push_button.set_sensitive(can_push)

    @Gtk.Template.Callback()
    def _pull_clicked(self, _widget):
        pull_action = PullAction.FETCH_AND_MERGE
        label = self.pull_button.get_label()
        if label == "Pull":
            pull_action = PullAction.FETCH_AND_MERGE
        elif label == "Fetch":
            pull_action = PullAction.FETCH_ONLY
        else:
            pull_action = PullAction.FETCH_AND_REBASE

        self._pull(pull_action=pull_action)

    @Gtk.Template.Callback()
    def _push_clicked(self, _widget):
        self._push()

    @Gtk.Template.Callback()
    def _refresh_clicked(self, widget):
        self.__refresh()

    @Gtk.Template.Callback()
    def _branch_changed_handler(self, _widget, _property):
        self.updating_model_from_signal = True
        self._branch_or_upstream_changed()
        self.__refresh()
        self.updating_model_from_signal = False

    @Gtk.Template.Callback()
    def _upstream_changed_handler(self, _widget, _property):
        self.updating_model_from_signal = True
        self._branch_or_upstream_changed()
        self.__refresh()
        self.updating_model_from_signal = False


if __name__ == "__main__":
    TurtleApp(SyncWindow).run()
