""" diff dialog

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
from turtlevcs.dialogs.commit_table import CommitTable

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, GObject, Gio


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/diff.ui")
class DiffWindow(Adw.ApplicationWindow, DialogBase, BasedOnBase):
    """ diff dialog """
    __gtype_name__ = "DiffWindow"
    __gsignals__ = {
        'branch-or-tag-created': (GObject.SignalFlags.RUN_FIRST, GObject.TYPE_NONE, ()),
    }

    refresh_button = Gtk.Template.Child()
    scolled_window = Gtk.Template.Child()

    path_entry = Gtk.Template.Child()
    file_open_button = Gtk.Template.Child()
    folder_open_button = Gtk.Template.Child()

    # source 1
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

    # source 2
    head_button2 = Gtk.Template.Child()
    branch_button2 = Gtk.Template.Child()
    commit_button2 = Gtk.Template.Child()
    branch_model2 = Gtk.Template.Child()

    based_on_row2 = Gtk.Template.Child()
    head_row2 = Gtk.Template.Child()
    branch_row2 = Gtk.Template.Child()
    commit_row2 = Gtk.Template.Child()
    commit_row_button2 = Gtk.Template.Child()
    specific_commit_row2 = Gtk.Template.Child()
    head_label2 = Gtk.Template.Child()
    specific_commit_label2 = Gtk.Template.Child()

    second_source_log = False

    diff_table = None

    open_dialog = None

    is_updating = False

    def __init__(self, path, _commit=None):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        BasedOnBase.__init__(self, with_working_copy=True)

        self.path_entry.set_text(path)
        self.path_entry.connect("changed", self._path_changed)

        self._set_title_repo(prefix="Diff")

        self.diff_table = CommitTable(self.turtle)
        self.diff_table.column_selected.set_visible(False)
        self.scolled_window.set_child(self.diff_table)

        self._based_on_changed_handler(self.head_button)
        self._based_on_changed_handler2(self.head_button2)
        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    def _based_on_changed(self, second_source=False):
        if second_source:
            self.specific_commit_row2.set_visible(False)
        else:
            self.specific_commit_row.set_visible(False)
        super()._based_on_changed(second_source)

    def _commit_search_response(self, widget):
        commit = widget.get_selected_commit()
        if self.second_source_log:
            self.commit_row2.set_text(commit.hex)
        else:
            self.commit_row.set_text(commit.hex)
        widget.close()

    def __update(self, quickupdate=False):
        self.is_updating = True
        self.refresh_button.set_sensitive(False)

        based_on_valid = True
        based_on_valid2 = True

        self.specific_commit_row.set_visible(False)
        self.specific_commit_row2.set_visible(False)

        if quickupdate is False:
            def update_dropdown(model):
                """ helper function to update both branch dropdowns """
                old_string = None
                old_selected = self.branch_row.get_selected_item()
                if old_selected:
                    old_string = old_selected.get_string()
                while model.get_n_items() > 0:
                    model.remove(0)
                branch_list = self.turtle.get_list_of_branches()
                index = 0
                selected_index = 0
                for branch in branch_list:
                    model.append(branch)
                    if branch == old_string:
                        selected_index = index
                    index = index + 1
                self.branch_row.set_selected(selected_index)

            update_dropdown(self.branch_model)
            update_dropdown(self.branch_model2)

        head_id = self.turtle.get_current_commit_hex()
        self.head_label.set_label(head_id)
        self.head_label2.set_label(head_id)

        based_on_valid = self._is_based_on_valid()
        based_on_valid2 = self._is_based_on_valid(second_source=True)

        if based_on_valid and based_on_valid2:

            revision1 = self._get_base_revision()
            revision2 = self._get_base_revision(second_source=True)
            if revision2 is None:
                diff = revision1.tree.diff_to_workdir()
            else:
                diff = revision1.tree.diff_to_tree(revision2.tree)
            diff.find_similar()

            path = self.path_entry.get_text()
            if len(path) > 0 and os.path.exists(path) and path.startswith(self.turtle.repo.workdir):
                path = path.removeprefix(self.turtle.repo.workdir)
            else:
                path = ""

            diff_list = []
            if diff:
                for patch in diff:
                    if patch.delta.new_file.path.startswith(path) \
                        or patch.delta.old_file.path.startswith(path):
                        diff_list.append((
                            patch.delta.status,
                            str(revision2.id if revision2 else None),
                            str(revision1.id),
                            patch.delta.new_file.path,
                            patch.delta.old_file.path))

            self.diff_table.update_model_with_diff([diff_list])
        else:
            self.diff_table.update_model_with_diff([])

        self.is_updating = False
        self.refresh_button.set_sensitive(True)

    @Gtk.Template.Callback()
    def _refresh_clicked(self, widget):
        if not self.is_updating:
            self._on_refresh_clicked()

    def _path_changed(self, _widget):
        self.__update(quickupdate=True)

    @Gtk.Template.Callback()
    def _path_entry_button_handler(self, widget):
        path_string = self.path_entry.get_text()

        if not self.open_dialog:
            self.open_dialog = Gtk.FileChooserNative.new(
                title="",
                parent=self, action=Gtk.FileChooserAction.OPEN)
            self.open_dialog.connect("response", self._open_path_callback)

        if widget == self.file_open_button:
            self.open_dialog.set_title("Select a file")
            self.open_dialog.set_action(Gtk.FileChooserAction.OPEN)
        else:
            self.open_dialog.set_title("Select a directory")
            self.open_dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)

        if len(path_string) > 0 and os.path.exists(path_string):
            path = Gio.File.new_for_path(path_string)
            if os.path.isfile(path_string):
                path = path.get_parent()
            self.open_dialog.set_current_folder(path)

        self.open_dialog.show()

    def _open_path_callback(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            path = dialog.get_file().get_path()
            if os.path.exists(path):
                if path.startswith(self.turtle.repo.workdir):
                    self.path_entry.set_text(path)
                else:
                    pass # TODO maybe show a toast

    @Gtk.Template.Callback()
    def _based_on_changed_handler(self, widget):
        if not self.is_updating and widget.get_active():
            self._based_on_changed()
            self.__update(quickupdate=True)

    @Gtk.Template.Callback()
    def _based_on_changed_handler2(self, widget):
        if not self.is_updating and widget.get_active():
            self._based_on_changed(second_source=True)
            self.__update(quickupdate=True)

    @Gtk.Template.Callback()
    def _branch_changed_handler(self, _widget, _property):
        if not self.is_updating:
            self._based_on_changed()
            self.__update(quickupdate=True)

    @Gtk.Template.Callback()
    def _branch_changed_handler2(self, _widget, _property):
        if not self.is_updating:
            self._based_on_changed(second_source=True)
            self.__update(quickupdate=True)

    @Gtk.Template.Callback()
    def _commit_entry_changed_handler(self, _widget):
        if not self.is_updating:
            self.__update(quickupdate=True)

    @Gtk.Template.Callback()
    def _commit_search_button_handler(self, widget):
        self.second_source_log = widget == self.commit_row_button2
        # pylint: disable=C0415
        # avoid circular dependency
        from turtlevcs.dialogs.log import LogWindow
        # pylint: enable=C0415
        log = LogWindow(self.turtle.repo.workdir, select_button_visible=True)
        log.connect("commit-selected", self._commit_search_response)
        log.set_transient_for(self)
        log.set_modal(True)
        log.set_visible(True)

    # @Gtk.Template.Callback()
    # def _path_entry_changed_handler(self):
    #     pass

    # @Gtk.Template.Callback()
    # def _path_search_button_handler(self):
    #     pass


if __name__ == "__main__":
    TurtleApp(DiffWindow).run()
