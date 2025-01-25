""" checkout dialog

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
from turtlevcs.dialogs.base import DialogBase, BasedOnBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/checkout.ui")
class CheckoutWindow(Adw.ApplicationWindow, DialogBase, BasedOnBase):
    """ checkout dialog """
    __gtype_name__ = "CheckoutWindow"

    checkout_button = Gtk.Template.Child()

    branch_button = Gtk.Template.Child()
    commit_button = Gtk.Template.Child()
    branch_model = Gtk.Template.Child()

    branch_row = Gtk.Template.Child()
    commit_row = Gtk.Template.Child()
    new_branch_button = Gtk.Template.Child()
    new_branch_entry = Gtk.Template.Child()
    force_button = Gtk.Template.Child()
    override_button = Gtk.Template.Child()

    is_updating = False
    checkout_commit_instead_of_branch = False

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        BasedOnBase.__init__(self)

        self._set_title_repo()

        self._based_on_changed_handler(self.branch_button)
        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    def __update(self, quickupdate=False):
        self.is_updating = True
        self.checkout_button.set_sensitive(False)

        if quickupdate is False:
            while self.branch_model.get_n_items() > 0:
                self.branch_model.remove(0)
            branch_list = self.turtle.get_list_of_branches()
            for branch in branch_list:
                self.branch_model.append(branch)

        new_branch = self.new_branch_button.get_active()
        self.new_branch_entry.set_sensitive(new_branch)
        self.override_button.set_sensitive(new_branch)

        based_on_valid = self._is_based_on_valid()
        branch_valid = \
            self.new_branch_button.get_active() is False \
                or len(self.new_branch_entry.get_text()) > 0

        # TODO maybe hide or not allow to checkout current branch / commit

        self.checkout_button.set_sensitive(based_on_valid and branch_valid)
        self.is_updating = False

    def __checkout(self):
        self.checkout_commit_instead_of_branch = self.commit_button.get_active()

        self._show_progress_window("Checkout", self._do_checkout)

    def _do_checkout(self):
        message = None
        name = self.branch_row.get_selected_item().get_string()
        if self.checkout_commit_instead_of_branch:
            name = self.commit_row.get_text()

        force = self.force_button.get_active()
        override = False
        new_branch_name = None
        if self.new_branch_button.get_active():
            new_branch_name = self.new_branch_entry.get_text()
            override = self.override_button.get_active()

        try:
            self.turtle.checkout(
                name,
                new_branch_name,
                force,
                override)
        except Exception as ex:
            message = str(ex)

        if message:
            summary = "Checkout Failed"
        else:
            checked_out = "commit" if self.checkout_commit_instead_of_branch else "branch"
            summary = "Checkout"
            message = f"Successfully checked out {checked_out}."

        self._set_progress_message(summary, details=message)

    def _progress_callback(self, message):
        pass

    def _commit_search_response(self, widget):
        commit = widget.get_selected_commit()
        self.commit_row.set_text(commit.hex)
        widget.close()

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        self.__checkout()

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

    @Gtk.Template.Callback()
    def _new_branch_toggled_handler(self, _widget):
        self.__update(quickupdate=True)


if __name__ == "__main__":
    TurtleApp(CheckoutWindow).run()
