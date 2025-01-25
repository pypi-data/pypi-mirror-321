""" commit dialog

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
import turtlevcs
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs import Question, MultilineInput
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs.commit_table import CommitTable, CommitSelection

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/commit.ui")
class CommitWindow(Adw.ApplicationWindow, DialogBase):
    """ commit dialog """
    __gtype_name__ = "CommitWindow"

    main_box = Gtk.Template.Child()
    header_bar = Gtk.Template.Child()
    commit_button = Gtk.Template.Child()
    amend = Gtk.Template.Child()
    gpg_sign = Gtk.Template.Child()
    message = Gtk.Template.Child()
    show_unversioned = Gtk.Template.Child()
    show_ignored = Gtk.Template.Child()
    scolled_window = Gtk.Template.Child()

    listview = None
    original_message = ""

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)

        self.listview = CommitTable(self.turtle, parent_window=self)
        self.scolled_window.set_child(self.listview)

        is_merge, _ = self.turtle.is_merge_in_progress()
        is_rebase, _ = self.turtle.is_rebase_in_progress()

        if is_merge or is_rebase:
            text = "This is a merge commit" if is_merge else "A rebase is in progress"
            # add a fallback for older versions of libadwaita
            if Adw.MINOR_VERSION > 2:
                self.banner = Adw.Banner()
                self.banner.set_title(text)
                self.banner.set_button_label("Ok")
                self.banner.connect("button-clicked", self._hide_banner)
            else:
                self.banner = Gtk.InfoBar()
                label = Gtk.Label()
                label.set_label(text)
                self.banner.add_child(label)
                self.banner.set_show_close_button(True)
                self.banner.connect("response", self._hide_banner)

            self.banner.set_revealed(True)
            self.main_box.insert_child_after(self.banner, self.header_bar)

        settings = turtlevcs.get_settings()
        self.show_unversioned.set_active(settings.get_boolean("commit-show-unversioned"))
        self.show_ignored.set_active(settings.get_boolean("commit-show-ignored"))
        self.gpg_sign.set_active(settings.get_boolean("gpg-auto-sign"))
        default_selection = CommitSelection(settings.get_enum("default-commit-selection"))
        self.__update(preselection=default_selection)
        self.file_list = None # reset preselection file_list
        self.set_focus(self.message)

    def update(self):
        """ public update function to be called from stage dialog """
        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    def _on_multiline_message_response(self, response, new_message):
        if response:
            self.message.set_text(new_message)

    def __update(self, amend_changed=False, preselection=CommitSelection.NONE):
        self.commit_button.set_sensitive(False)

        amend = self.amend.get_active()

        status, amend_message = self.turtle.get_commit_info(
            show_unversioned=self.show_unversioned.get_active(),
            show_ignored=self.show_ignored.get_active(),
            amend=amend
        )

        self._set_title_branch()

        if amend_changed:
            if amend:
                self.original_message = self.message.get_text()
                self.message.set_text(amend_message.strip())
            else:
                self.message.set_text(self.original_message)

        can_commit = self.listview.update_model_with_status(
            status, preselection=preselection, preselection_list=self.file_list)

        self.commit_button.set_sensitive(can_commit or amend)

    def __commit(self, response=True):
        if response:
            self._show_progress_window("Committing", self._do_commit)

    def _do_commit(self):
        message = self.message.get_text()
        amend = self.amend.get_active()
        files = []
        deleted_files = []

        count = self.listview.model.get_n_worktree_items()
        i = 0
        while i < count:
            item = self.listview.model.get_worktree_item(i)
            i += 1
            if item.selected:
                if item.status == pygit2.enums.FileStatus.WT_DELETED:
                    deleted_files.append(item.path)
                else:
                    files.append(item.path)

        settings = turtlevcs.get_settings()
        gpg_key = settings.get_string("gpg-key")
        total, error = self.turtle.commit(
            message, amend, files, deleted_files, self.gpg_sign.get_active(), gpg_key)

        if total > 0:
            summary = "Commited"
            error = f"{total} file(s) committed"
        elif total < 0:
            summary = "Committed"
            error = "Initial commit"
        elif amend:
            summary = "Commit message updated"
        else:
            summary = "No files committed"

        self._set_progress_message(summary, error)

    @Gtk.Template.Callback()
    def _ok_clicked(self, widget):
        if len(self.message.get_text()) == 0:
            question = Question(
                "Commit Empty Message?",
                message="The commit message is currently empty.",
                callback=self.__commit,
                parent=self)
            question.present()
        else:
            self.__commit()

    @Gtk.Template.Callback()
    def _refresh_clicked(self, widget):
        self.__update()

    def _hide_banner(self, _widget, _response_id=None):
        self.banner.set_visible(False)

    @Gtk.Template.Callback()
    def _message_entry_button_handler(self, _widget):
        dialog = MultilineInput(
            message=self.message.get_text(),
            callback=self._on_multiline_message_response,
            parent=self)
        dialog.present()

    @Gtk.Template.Callback()
    def _amend_toggle_handler(self, _widget):
        self.__update(amend_changed=True)

    @Gtk.Template.Callback()
    def _show_unversioned_toggle_handler(self, _widget):
        self.__update()

    @Gtk.Template.Callback()
    def _show_ignored_toggle_handler(self, _widget):
        self.__update()


if __name__ == "__main__":
    TurtleApp(CommitWindow).run()
