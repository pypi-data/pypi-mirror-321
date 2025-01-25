""" merge dialog

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


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/merge.ui")
class MergeWindow(Adw.ApplicationWindow, DialogBase, BasedOnBase):
    """ merge dialog """
    __gtype_name__ = "MergeWindow"

    merge_button = Gtk.Template.Child()

    branch_button = Gtk.Template.Child()
    commit_button = Gtk.Template.Child()
    branch_model = Gtk.Template.Child()

    branch_row = Gtk.Template.Child()
    commit_row = Gtk.Template.Child()
    ff_only_button = Gtk.Template.Child()
    no_ff_button = Gtk.Template.Child()

    is_updating = False
    merge_commit_instead_of_branch = False

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
        self.merge_button.set_sensitive(False)

        if quickupdate is False:
            while self.branch_model.get_n_items() > 0:
                self.branch_model.remove(0)
            branch_list = self.turtle.get_list_of_branches()
            for branch in branch_list:
                self.branch_model.append(branch)

        based_on_valid = self._is_based_on_valid()

        self.merge_button.set_sensitive(based_on_valid)
        self.is_updating = False

    def __merge(self):
        self._show_progress_window("Merging", self._do_merge)

    def _do_merge(self):
        message = None
        summary = None

        try:
            branch_name = None
            commit_hash = None
            if self.branch_button.get_active():
                branch_name = self.branch_row.get_selected_item().get_string()
            else:
                commit_hash = self.commit_row.get_text()

            ff_only = self.ff_only_button.get_active()
            no_ff = self.no_ff_button.get_active()

            message, summary = self.turtle.merge(branch_name, commit_hash, ff_only, no_ff)
        except Exception as ex:
            message = str(ex)

        if message:
            if summary is None or len(summary) == 0:
                summary = "Merge Failed"
        else:
            merged = "commit" if self.merge_commit_instead_of_branch else "branch"
            summary = "Merged"
            message = f"Successfully merged {merged}."

        self._set_progress_message(summary, details=message)

    def _progress_callback(self, message):
        pass

    def _commit_search_response(self, widget):
        commit = widget.get_selected_commit()
        self.commit_row.set_text(commit.hex)
        widget.close()

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        self.__merge()

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


if __name__ == "__main__":
    TurtleApp(MergeWindow).run()
