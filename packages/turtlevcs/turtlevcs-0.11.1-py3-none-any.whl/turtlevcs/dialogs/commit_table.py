""" commit table

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
from pygit2 import enums
import tempfile
from enum import Enum
import gi
import turtlevcs
from turtlevcs.dialogs import Notification, Question, Subprocess
from turtlevcs.dialogs.base import PopoverBase
from turtlevcs.dialogs.stage import StageDialog, StageConfirmDialog

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Gio, GObject

class CommitSelection(Enum):
    """ enum type for commit selection """
    NONE = 0
    SELECTED = 1
    ALL = 2


class CommitListModelEntryBase(GObject.Object):
    """ commit model entry base class, used for staged/tree headers """

    selected = False
    path = None
    old_path = None

    def __init__(self, path, old_path=None):
        GObject.Object.__init__(self)

        self.path = path
        self.old_path = old_path
        if self.old_path is None:
            self.old_path = self.path

    def get_path(self):
        """ get path string, including old path if renamed """
        if self.old_path and self.path != self.old_path:
            return f"{self.old_path} → {self.path}"
        else:
            return self.path

class CommitListModelEntry(CommitListModelEntryBase):
    """ an entry in the commit model, which represents a single file """
    hex = None
    parent_hex = None
    status = 0
    is_committed = 0
    is_staged = False
    controller = None

    def __init__(self, path, status, commit_hex=None, parent_hex=None, is_committed=False, old_path=None):
        CommitListModelEntryBase.__init__(self, path, old_path)
        self.status = status
        self.hex = commit_hex
        self.parent_hex = parent_hex
        self.is_committed = is_committed

        if isinstance(self.status, enums.FileStatus):
            is_staged, _ = turtlevcs.has_index_status(self.status)
            self.is_staged = not self.is_committed and is_staged
        self.selected = self.is_staged

    def set_selected(self, widget):
        """ (de)select this file to be committed """
        self.selected = widget.get_active()


class CommitListModel(GObject.Object, Gio.ListModel):
    """ commit model, contains files to commit """

    is_diff_model = False # False: commit, True: log, diff
    staged_items = []
    items = []
    hide_worktree_header = True

    def __init__(self):
        GObject.Object.__init__(self)

    def do_get_item(self, position):
        """ get item in model """
        if self.is_diff_model:
            if position < len(self.items):
                return self.items[position]
            return None

        if position < len(self.staged_items):
            return self.staged_items[position]

        position = position - len(self.staged_items)

        # hide Working Tree header if no staged items are availabe
        if self.hide_worktree_header:
            position = position + 1

        if position < len(self.items):
            return self.items[position]

        return None

    def do_get_item_type(self):
        """ get model item type """
        return type(CommitListModelEntryBase)

    def do_get_n_items(self):
        """ get model item list length """
        if self.is_diff_model:
            return len(self.items)

        n = len(self.staged_items) + len(self.items)

        # hide Working Tree header if no staged items are availabe
        if n > 0 and self.hide_worktree_header:
            n = n - 1

        return n

    def get_n_worktree_items(self):
        """ get number of worktree / non staged items """
        return len(self.items)

    def get_worktree_item(self, position):
        """ get worktree / non staged item ad index """
        if position < len(self.items):
            return self.items[position]

        return None

    def add(self, item):
        """ add an item to the model list """

        if self.is_diff_model:
            n_old = len(self.items)
            self.items.append(item)
            n_new = len(self.items)
        else:
            if item.is_staged:
                n_old = len(self.staged_items)
                if len(self.staged_items) == 0:
                    self.hide_worktree_header = False
                    self.items_changed(0, 0, 1)
                    self.staged_items.append(CommitListModelEntryBase("Staged"))
                self.staged_items.append(item)

                n_new = len(self.staged_items)
            else:
                n_old = self.do_get_n_items()
                if len(self.items) == 0:
                    self.items.append(CommitListModelEntryBase("Working Tree"))
                self.items.append(item)
                n_new = self.do_get_n_items()

        self.items_changed(n_old, 0, n_new - n_old)

    def clear(self):
        """ remove all items """
        n_old = self.do_get_n_items()
        self.items.clear()
        self.staged_items.clear()
        self.hide_worktree_header = True

        self.items_changed(0, n_old, 0)

    def select_all(self, select):
        """ select all items """
        for item in self.items:
            item.selected = select

    def all_selected(self):
        """ check if all items are selected """
        for item in self.items:
            if isinstance(item, CommitListModelEntry) and not item.selected:
                return False

        return len(self.items) > 0


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/commit_table.ui")
class CommitTable(Gtk.ColumnView, PopoverBase):
    """ commit dialog """
    __gtype_name__ = "CommitTable"

    turtle = None
    parent_window = None
    model = CommitListModel()
    select_all_checkbox = None
    selection_model = Gtk.Template.Child()
    column_selected = Gtk.Template.Child()

    def __init__(self, turtle, parent_window=None):
        Gtk.ColumnView.__init__(self)
        PopoverBase.__init__(self)

        self.turtle = turtle

        if parent_window is not None:
            self.parent_window = parent_window
            parent_window._add_action("action-unstage-file", self._unstage_file_from_popover)
            parent_window._add_action("action-revert-file", self._revert_file_from_popover)
            parent_window._add_action("action-stage-file", self._stage_file_from_popover)

        # TODO implement selection model to make headers non selectable,
        # or use header-factory introduced in Gtk 4.12
        self.selection_model.set_model(self.model)

        # TODO find a better way to do this
        try:
            self.select_all_checkbox = Gtk.CheckButton()
            child = self.get_first_child()
            while child is not None:
                name = child.__class__.__name__
                if name in ["GtkColumnViewRowWidget", "GtkListItemWidget"]:
                    row_title = child.get_first_child()
                    box = row_title.get_first_child()
                    label = box.get_first_child()
                    if label is not None:
                        title = label.get_text()
                        if title == "":
                            box.remove(label)
                            box.append(self.select_all_checkbox)
                            gesture = Gtk.GestureClick()
                            gesture.connect("pressed", self._select_all)
                            row_title.add_controller(gesture)
                            break
                child = child.get_next_sibling()
        except Exception as _ex:
            pass

    def update_model_with_status(self,
            status,
            hide_staged=False,
            preselection=CommitSelection.NONE,
            preselection_list=None):
        """ set the current commits from a status list """
        self.model.is_diff_model = False

        old_items = self.model.items.copy()
        self.model.clear()

        for file in status:
            file_status = status[file]
            is_staged, index_status = turtlevcs.has_index_status(file_status)
            if is_staged and not hide_staged:
                entry = CommitListModelEntry(path=file, status=index_status)
                self.model.add(entry)

            is_wt, wt_status = turtlevcs.has_worktree_status(file_status)
            if is_wt:
                entry = CommitListModelEntry(path=file, status=wt_status)
                # find_with_equal_func is currently broken
                # see https://gitlab.gnome.org/GNOME/pygobject/-/issues/493
                old = None

                if preselection != CommitSelection.NONE:
                    if preselection == CommitSelection.SELECTED:
                        # get selection state from preselection list
                        if preselection_list is not None and \
                            any(file.startswith(p) for p in preselection_list):
                            entry.selected = True
                    else:
                        entry.selected = True
                else:
                    # get selection state from old model
                    count = len(old_items)
                    i = 0
                    while i < count:
                        old = old_items[i]
                        if old.path == entry.path:
                            break
                        i += 1
                    if i < count:
                        entry.selected = old.selected

                self.model.add(entry)

        self._update_all_selected()

        return self.model.get_n_items()

    def update_model_with_diff(self, diffs, is_committed=False):
        """ set the current commits from a diff list """
        self.model.is_diff_model = True

        self.model.clear()

        show_headers = len(diffs) > 1
        for diff in diffs:
            if show_headers:
                try:
                    (_, _, commit_hex, _, _) = diff[0]
                    self.model.add(CommitListModelEntryBase(f"Diff to {commit_hex}"))
                except Exception:
                    pass
            for status, commit_hex, parent_hex, new_path, old_path in diff:
                entry = CommitListModelEntry(
                    path=new_path,
                    old_path=old_path,
                    status=status,
                    commit_hex=commit_hex,
                    parent_hex=parent_hex,
                    is_committed=is_committed)
                self.model.add(entry)

    def _select_all(self, _gesture, _n_press, _x, _y):
        self.select_all_checkbox.activate()
        self.model.select_all(self.select_all_checkbox.get_active())
        self.parent_window.update()

    def _update_all_selected(self, _widget=None):
        self.select_all_checkbox.set_active(self.model.all_selected())

    def _unstage_file_from_popover(self, _widget, data):
        name = data.get_string()
        question = Question(
            "Unstage",
            message=f"Do you want to unstage '{name}'?",
            callback=self._unstage_file_from_popover_callback,
            data=name,
            parent=self.parent_window)
        question.present()

    def _unstage_file_from_popover_callback(self, response, path):
        if response:
            self.turtle.unstage(path)

        self.parent_window.update()

    def _revert_file_from_popover(self, _widget, data):
        name = data.get_string()
        _, wt_new = self.turtle.can_be_reverted(name)
        question = Question(
            "Revert",
            message=f"Do you want to {'delete' if wt_new else 'revert'} '{name}'?",
            callback=self._revert_file_from_popover_callback,
            data=name,
            parent=self.parent_window)
        question.present()

    def _revert_file_from_popover_callback(self, response, path):
        if response:
            self.turtle.revert(path)

        self.parent_window.update()

    def _stage_file_from_popover(self, _widget, data):
        try:
            file = data.get_string()
            settings = turtlevcs.get_settings()
            show_stage_info = settings.get_boolean("stage-show-information")

            path = str(self.turtle.get_full_file_path(file))
            if show_stage_info:
                dialog = StageDialog(
                    path, parent=self.parent_window, show_confirmation=False)
            else:
                dialog = StageConfirmDialog(
                    self.turtle, path, parent=self.parent_window, show_confirmation=False)

            self.parent_window.show_new_window(dialog, close=False)
        except Exception as ex:
            notification = Notification(str(ex), title="Failed Stage", parent=self.parent_window)
            notification.set_visible(True)

    @Gtk.Template.Callback()
    def _listview_activated_handler(self, _widget, position):
        temp1 = None
        temp2 = None
        path1 = None
        path2 = None
        try:
            item = self.model.get_item(position)
            if isinstance(item, CommitListModelEntry):
                if self.model.is_diff_model and item.hex:
                    if item.parent_hex:
                        temp1 = self.turtle.get_file_from_commit(item.parent_hex, item.old_path)
                        path1 = temp1.name
                    else:
                        # TODO find a better way to do this
                        temp1 = tempfile.NamedTemporaryFile(suffix=f"__-_{item.old_path}")
                        path1 = temp1.name
                    if item.hex == str(None):
                        path2 = self.turtle.get_full_file_path(item.path)
                    else:
                        temp2 = self.turtle.get_file_from_commit(item.hex, item.path)
                        path2 = temp2.name
                else:
                    if item.is_staged:
                        temp1 = self.turtle.get_file_from_previous_commit(item.old_path)
                        path1 = temp1.name
                        temp2 = self.turtle.get_file_from_index(item.path)
                        path2 = temp2.name
                    else:
                        temp1 = self.turtle.get_file_from_index(item.old_path)
                        path1 = temp1.name
                        path2 = self.turtle.get_full_file_path(item.path)

                subprocess = Subprocess(["meld", path1, path2], self.parent_window)
                # store temp file objects in dialog to keep them alive
                subprocess.temp_file1 = temp1
                subprocess.temp_file2 = temp2
                subprocess.present()
        except Exception as _ex:
            # TODO show dialog with error
            pass

    @Gtk.Template.Callback()
    def _column_selected_setup_handler(self, _factory, listitem):
        # TODO enter press will be captured by the checkbutton
        # prevent this so the diff opens on enter press
        checkbox = Gtk.CheckButton()
        listitem.set_child(checkbox)

    @Gtk.Template.Callback()
    def _column_selected_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        checkbox = listitem.get_child()
        if isinstance(item, CommitListModelEntry):
            checkbox.set_active(item.selected)
            checkbox.set_sensitive(not item.is_staged)
            checkbox.connect("toggled", item.set_selected)
            checkbox.connect("toggled", self._update_all_selected)
        else:
            checkbox.set_visible(False)

    @Gtk.Template.Callback()
    def _column_path_setup_handler(self, _factory, listitem):
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        label.set_hexpand(True)
        box.append(label)
        listitem.set_child(box)

    @Gtk.Template.Callback()
    def _column_path_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        box = listitem.get_child()
        label = box.get_first_child()
        label.set_label(item.get_path())
        if isinstance(item, CommitListModelEntry):
            if not self.model.is_diff_model:
                def gesture_pressed_row(gesture, _n_press, _x, _y):
                    box = gesture.get_widget()

                    popover = None
                    child = box.get_first_child()
                    while child:
                        if isinstance(child, Gtk.PopoverMenu):
                            popover = child
                            break
                        child = child.get_next_sibling()

                    entries = []

                    if item.is_staged:
                        entries.append(("Unstage",
                                        "win.action-unstage-file",
                                        item.path))
                    else:
                        can_revert = self.turtle.can_be_reverted(item.path)
                        path = str(self.turtle.get_full_file_path(item.path))
                        can_stage, _ = self.turtle.can_be_staged(path)

                        entries.append(("Revert",
                                        "win.action-revert-file" if can_revert else "dummy",
                                        item.path))
                        entries.append(("Stage",
                                        "win.action-stage-file" if can_stage else "dummy",
                                        item.path))

                    self._create_popover(box, entries, popover)

                item.controller = self._add_popover_gesture(box, gesture_pressed_row)
        else:
            label.set_sensitive(False)

    @Gtk.Template.Callback()
    def _column_path_unbind_handler(self, _factory, listitem):
        item = listitem.get_item()
        box = listitem.get_child()

        if isinstance(item, CommitListModelEntry):
            if item.controller is not None:
                widget = item.controller.get_widget()
                if widget is box:
                    box.remove_controller(item.controller)
                item.controller = None

    @Gtk.Template.Callback()
    def _column_status_setup_handler(self, _factory, listitem):
        box = Gtk.Box()
        box.set_halign(Gtk.Align.CENTER)
        listitem.set_child(box)

    @Gtk.Template.Callback()
    def _column_status_teardown_handler(self, _factory, listitem):
        listitem.set_child(None)

    @Gtk.Template.Callback()
    def _column_status_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        box = listitem.get_child()

        if isinstance(item, CommitListModelEntry):
            if isinstance(item.status, enums.DeltaStatus):
                status_map = turtlevcs.delta_status_icon_map
            else:
                status_map = turtlevcs.status_icon_map

            if item.status in status_map:
                box.append(Gtk.Image.new_from_icon_name(status_map[item.status]))
            else:
                # if multiple status bits are set, chose the first one TODO show all
                for key, status in status_map.items():
                    if key > 0 and item.status & key:
                        box.append(Gtk.Image.new_from_icon_name(status))

    @Gtk.Template.Callback()
    def _column_status_unbind_handler(self, _factory, listitem):
        box = listitem.get_child()
        child = box.get_first_child()
        while child is not None:
            box.remove(child)
            child = box.get_first_child()
