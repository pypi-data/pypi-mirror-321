""" create dialog

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
from enum import Enum
import gi
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase, BasedOnBase, CreateFrom

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, GObject


class CreateType(Enum):
    """ enum to specify the create dialog type"""
    BRANCH = 0,
    TAG = 1

@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/create.ui")
class CreateWindow(Adw.ApplicationWindow, DialogBase, BasedOnBase):
    """ create branch or tag dialog """
    __gtype_name__ = "CreateWindow"
    __gsignals__ = {
        'branch-or-tag-created': (GObject.SignalFlags.RUN_FIRST, GObject.TYPE_NONE, ()),
    }

    create_button = Gtk.Template.Child()

    name_entry = Gtk.Template.Child()
    annotation_entry = Gtk.Template.Child()

    tag_type_row = Gtk.Template.Child()
    lightweight_button = Gtk.Template.Child()
    annotated_button = Gtk.Template.Child()

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

    settings_row = Gtk.Template.Child()
    checkout = Gtk.Template.Child()
    force = Gtk.Template.Child()

    type = CreateType.BRANCH
    specific_commit = None

    def __init__(self, path, create_type=CreateType.BRANCH, commit=None):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        BasedOnBase.__init__(self)

        self._set_title_repo()

        self.type = create_type
        self.specific_commit = commit

        if self.type is CreateType.BRANCH:
            self.name_entry.set_title("Branch Name")
            self.tag_type_row.set_visible(False)
            self.annotation_entry.set_visible(False)
        else:
            self.name_entry.set_title("Tag Name")
            self.settings_row.set_visible(False)
            self._tag_type_changed_handler(self.annotated_button)

        self._based_on_changed_handler(self.head_button)
        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    def _based_on_changed(self, second_source=False):
        if self.specific_commit:
            self.based_on_row.set_visible(False)
            self.head_row.set_visible(False)
            self.head_row.set_visible(False)
            self.branch_row.set_visible(False)
            self.commit_row.set_visible(False)
            self.specific_commit_row.set_visible(True)
            self.source = CreateFrom.COMMIT
        else:
            self.specific_commit_row.set_visible(False)
            super()._based_on_changed()

    def __update(self, quickupdate=False):
        self.create_button.set_sensitive(False)

        based_on_valid = True
        name_valid = len(self.name_entry.get_text()) > 0

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

        self.create_button.set_sensitive(based_on_valid and name_valid)

    def __create(self):
        type_name = "Branch" if self.type else "Tag"
        self._show_progress_window(f"Creating {type_name}", self._do_create)

    def _do_create(self):
        title = "Done"
        summary = "Nothing has been created"
        name = self.name_entry.get_text()
        checkout = self.checkout.get_active()
        try:
            if self.type is CreateType.BRANCH:
                self.turtle.create_branch(
                    name,
                    self.source,
                    self.specific_commit if self.specific_commit else self._get_base(),
                    checkout,
                    self.force.get_active())
            elif self.type is CreateType.TAG:
                is_annotated = self.annotated_button.get_active()
                self.turtle.create_tag(
                    name,
                    self.source,
                    self.specific_commit if self.specific_commit else self._get_base(),
                    self.annotation_entry.get_text() if is_annotated else None
                )

            title = "Created"
            summary = f"{'Branch' if self.type is CreateType.BRANCH else 'Tag'} " \
                f"'{name}' has been created"
            if checkout:
                summary += " and checked out"
            self.emit("branch-or-tag-created")
        except Exception as ex:
            title = "Error"
            summary = str(ex)

        self._set_progress_message(title, summary)

    def _commit_search_response(self, widget):
        commit = widget.get_selected_commit()
        self.commit_row.set_text(commit.hex)
        widget.close()

    @Gtk.Template.Callback()
    def _ok_clicked(self, _widget):
        self.__create()

    @Gtk.Template.Callback()
    def _branch_name_changed(self, _widget):
        self.__update()

    @Gtk.Template.Callback()
    def _annotation_changed(self, _widget):
        self.__update()

    @Gtk.Template.Callback()
    def _based_on_changed_handler(self, widget):
        if widget.get_active():
            self._based_on_changed()
            self.__update()

    @Gtk.Template.Callback()
    def _tag_type_changed_handler(self, _widget):
        is_annotated = self.annotated_button.get_active()
        self.annotation_entry.set_sensitive(is_annotated)
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
    TurtleApp(CreateWindow).run()
