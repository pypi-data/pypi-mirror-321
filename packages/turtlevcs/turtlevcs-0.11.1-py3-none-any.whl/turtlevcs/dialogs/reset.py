""" reset dialog

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
import pygit2
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase, BasedOnBase
from turtlevcs.dialogs import Notification

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, GObject


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/reset.ui")
class ResetWindow(Adw.ApplicationWindow, DialogBase, BasedOnBase):
    """ reset dialog """
    __gtype_name__ = "ResetWindow"
    __gsignals__ = {
        'reset': (GObject.SignalFlags.RUN_FIRST, GObject.TYPE_NONE, ()),
    }

    reset_button = Gtk.Template.Child()

    commit_type_row = Gtk.Template.Child()
    # soft_button = Gtk.Template.Child()
    # mixed_button = Gtk.Template.Child()
    # hard_button = Gtk.Template.Child()

    head_button = Gtk.Template.Child()
    branch_button = Gtk.Template.Child()
    commit_button = Gtk.Template.Child()
    branch_model = Gtk.Template.Child()

    based_on_row = Gtk.Template.Child()
    head_row = Gtk.Template.Child()
    branch_row = Gtk.Template.Child()
    commit_row = Gtk.Template.Child()
    specific_commit_row = Gtk.Template.Child()
    head_label = Gtk.Template.Child()
    specific_commit_label = Gtk.Template.Child()

    specific_commit = None

    def __init__(self, path, commit=None):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        BasedOnBase.__init__(self)

        self._set_title_repo()

        self.specific_commit = commit

        self._based_on_changed_handler(self.head_button)

    def _on_cancel_clicked(self):
        self.close()

    def _based_on_changed(self, second_source=False):
        if self.specific_commit:
            self.based_on_row.set_visible(False)
            self.head_row.set_visible(False)
            self.head_row.set_visible(False)
            self.branch_row.set_visible(False)
            self.commit_row.set_visible(False)
            self.specific_commit_row.set_visible(True)
        else:
            self.specific_commit_row.set_visible(False)
            super()._based_on_changed()

    @Gtk.Template.Callback()
    def _reset_clicked(self, _widget):
        self.turtle.reset(
            self.specific_commit if self.specific_commit else self._get_base(),
            pygit2.enums.ResetMode(self.commit_type_row.get_selected() + 1))
        self.emit("reset")
        self.close()

    @Gtk.Template.Callback()
    def _based_on_changed_handler(self, widget):
        if widget.get_active():
            self._based_on_changed()
            self.__update()

    @Gtk.Template.Callback()
    def _commit_entry_changed_handler(self, _widget):
        self.__update(quickupdate=True)

    @Gtk.Template.Callback()
    def _commit_search_button_handler(self, _widget):
        # pylint: disable=C0415
        # avoid circular dependency
        from turtlevcs.dialogs.log import LogWindow
        # pylint: enable=C0415
        log = LogWindow(self.turtle.repo.workdir, select_button_visible=True)
        log.connect("commit-selected", self._commit_search_response)
        log.set_transient_for(self)
        log.set_modal(True)
        log.set_visible(True)

    def _commit_search_response(self, widget):
        commit = widget.get_selected_commit()
        self.commit_row.set_text(commit.hex)
        widget.close()

    def __update(self, quickupdate=False):
        self.reset_button.set_sensitive(False)
        based_on_valid = self._is_based_on_valid()

        if self.specific_commit:
            self.specific_commit_label.set_text(self.specific_commit)
        else:
            self.specific_commit_row.set_visible(False)

            if quickupdate is False:
                while self.branch_model.get_n_items() > 0:
                    self.branch_model.remove(0)
                branch_list = self.turtle.get_list_of_branches()
                for branch in branch_list:
                    self.branch_model.append(branch)

            head_id = self.turtle.get_current_commit_hex()
            self.head_label.set_label(head_id)

            based_on_valid = self._is_based_on_valid()

        self.reset_button.set_sensitive(based_on_valid)


if __name__ == "__main__":
    TurtleApp(ResetWindow).run()
