""" log dialog

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
from datetime import datetime, timezone
import math
import configparser
import pygit2
import gi
from turtlevcs.colors import get_theme_colors, get_theme_color_by_index
from turtlevcs.turtle import PullAction, verify_message
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase, PopoverBase
from turtlevcs.dialogs.commit_table import CommitTable
from turtlevcs.dialogs import Notification, Question, QuickSettings

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gdk, Gio, GLib, GObject

GRAPH_LINE_WIDTH = 18

class LogListModelEntry(GObject.Object):
    """ an entry in the push model, which represents a single commit """
    date = None
    short_id = None
    hex = None
    message = None
    message_full = None
    author = None
    gpg_signature = None
    diff = None
    node = -1
    lines = []
    old_lines = []
    color = -1
    controller = None

    def __init__(self, short_id, commit_hex, message, author, date, gpg_signature=None):
        GObject.Object.__init__(self)
        self.short_id = short_id
        self.hex = commit_hex
        # strip potential newlines from message
        self.message_full = message.strip()
        self.message = self.message_full.split("\n")[0]
        self.author = author
        if gpg_signature and gpg_signature[0] and gpg_signature[1]:
            try:
                signer = verify_message(gpg_signature[1].decode(), gpg_signature[0].decode())
                self.gpg_signature = f"signed by \"{signer}\"\n" if signer else "invalid signature\n"
            except Exception as _ex:
                pass # dbus/seahorse might not be installed
        if date:
            timestamp = datetime.fromtimestamp(date, timezone.utc).astimezone()
            time_diff = datetime.now(timezone.utc).astimezone() - timestamp
            if time_diff.days < 1:
                self.date = timestamp.strftime("%H:%M")
            elif time_diff.days < 7:
                self.date = timestamp.strftime("%a, %H:%M")
            else:
                self.date = timestamp.strftime("%Y-%m-%d")

    def set_diff(self, diff):
        """ set_diff """
        self.diff = diff

    def set_line_data(self, node, lines, old_lines, color):
        """ set_line_data """
        self.node = node
        self.lines = lines
        self.old_lines = old_lines
        self.color = color


class LogListModel(GObject.Object, Gio.ListModel):
    """ push model contains commits to push """
    maximum = 0 # maximum number of lines in the graph
    items = []

    def __init__(self):
        GObject.Object.__init__(self)

    def do_get_item(self, position):
        """ get item in model """
        if position < len(self.items):
            return self.items[position]

        return None

    def do_get_item_type(self):
        """ get model item type """
        return type(LogListModelEntry)

    def do_get_n_items(self):
        """ get model item list length """
        return len(self.items)

    def set_items(self, items):
        """ update model items """
        old_length = len(self.items)
        self.items = items
        self.items_changed(0, old_length, len(self.items))


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/log_filter.ui")
class LogFilter(Gtk.Box):
    """ log filter widget """
    __gtype_name__ = "LogFilter"

    hidden_sources = Gtk.Template.Child()

    remotes_switches = {}
    local_switch = None

    def __init__(self, available_remotes, hidden_remotes, hide_local):
        Gtk.Box.__init__(self)

        # add local
        row = Adw.ActionRow()
        row.set_selectable(False)
        row.set_title("Local")
        row.set_subtitle("Local Branches")

        self.local_switch = Gtk.Switch()
        self.local_switch.set_valign(Gtk.Align.CENTER)
        self.local_switch.set_active(not hide_local)
        row.add_suffix(self.local_switch)

        self.hidden_sources.append(row)

        # add remotes
        for remote in available_remotes:
            row = Adw.ActionRow()
            row.set_selectable(False)
            row.set_title(remote.name)
            row.set_subtitle(remote.url)

            switch = Gtk.Switch()
            switch.set_valign(Gtk.Align.CENTER)
            switch.set_active(remote.name not in hidden_remotes)
            row.add_suffix(switch)
            self.remotes_switches[remote.name] = switch

            self.hidden_sources.append(row)

    def get_hidden_remotes(self):
        """ get a list of all remotes that have been deselected """
        hidden_remotes = []

        for remote, switch in self.remotes_switches.items():
            if switch.get_active() is False:
                hidden_remotes.append(remote)

        hide_local = not self.local_switch.get_active()

        return hidden_remotes, hide_local


class LogCalculator():
    """
    log calculator
    contains all functions necessary to calculate the graph
    which will also be used for log tests
    """

    branch_colors_in_use = []
    branch_connections = {}

    selected_commit_hex = None
    last_selected_commit = 0

    def __calculate_branch_connection_colors(self, revisions, old_lines):
        for i, _ in enumerate(revisions):
            for _, end, old_index in old_lines:
                if end == i:
                    if i not in self.branch_connections:
                        self.branch_connections[i] = old_index
                        self.branch_colors_in_use[old_index] += 1
                        break

    def __get_next_color_index(self, i):
        color_found = False
        index = -1
        if i in self.branch_connections:
            index = self.branch_connections.pop(i)
            color_found = True

        if not color_found:
            # colors may be used multiple times, find the (first) least used one
            lowest_color_index = self.branch_colors_in_use[0]
            for i in self.branch_colors_in_use:
                if i < lowest_color_index:
                    lowest_color_index = i

            index = self.branch_colors_in_use.index(lowest_color_index)
            self.branch_colors_in_use[index] += 1

        return index

    def calculate_graph(self, commit_list, model_list):
        """ calculate the graph model list """
        maximum = 0
        revisions = []
        old_lines = []
        for commit in commit_list:
            entry = LogListModelEntry(
                short_id=commit.short_id,
                commit_hex=str(commit.id),
                message=commit.message,
                author=commit.author.name,
                date=commit.commit_time,
                gpg_signature=commit.gpg_signature)

            # calculate graph data
            parents = []
            for parent in commit.parents:
                parents.append(parent)

            if commit not in revisions:
                revisions.append(commit)

            index = revisions.index(commit)
            next_revisions = revisions[:]

            parents_to_add = []
            for parent in parents:
                if parent not in next_revisions:
                    parents_to_add.append(parent)

            next_revisions[index : index + 1] = parents_to_add

            lines = []
            node_color_index = -2 # fallback color index, should never be used
            self.branch_colors_in_use = []
            for _ in get_theme_colors():
                self.branch_colors_in_use.append(0)
            self.branch_connections = {}

            self.__calculate_branch_connection_colors(revisions, old_lines)

            for i, revision in enumerate(revisions):
                color_index = -1 # fallback color index, in case of too many branches
                if revision in next_revisions:
                    color_index = self.__get_next_color_index(i)
                    if i == index:
                        node_color_index = color_index
                    lines.append((i, next_revisions.index(revision), color_index))
                elif revision == commit:
                    for parent in parents:
                        old_i = next_revisions.index(parent)

                        color_index = self.__get_next_color_index(i)
                        if old_i == index:
                            node_color_index = color_index
                        elif node_color_index == -2 and i == index:
                            node_color_index = color_index
                        lines.append((i, old_i, color_index))

            # special case for node color of very first commit
            if node_color_index == -2:
                for start, end, color_index in old_lines:
                    if start == index and end == index:
                        node_color_index = color_index
                        break
            entry.set_line_data(index, lines, old_lines, node_color_index)
            revisions = next_revisions
            old_lines = lines

            if len(entry.lines) > maximum:
                maximum = len(entry.lines)

            model_list.append(entry)

            if str(commit.id) == self.selected_commit_hex and len(model_list) > 0:
                self.last_selected_commit = len(model_list) - 1

        return maximum

    def calculate_diff_for_commit(self, entry, commit):
        """ calculate diff to previous commit(s) """
        def add_diff_to_list(diff, diffs):
            if diff is not None and diffs is not None:
                for patch in diff:
                    diffs.append((
                        patch.delta.status,
                        str(commit.id),
                        parent_hex,
                        patch.delta.new_file.path,
                        patch.delta.old_file.path))

        # get commit and file name of diff
        diff = None
        list_of_diffs = []
        parent_hex = None
        if len(commit.parents) > 0:
            for parent in commit.parents:
                diffs = []
                parent_hex = str(parent.id)
                diff = parent.tree.diff_to_tree(commit.tree)
                diff.find_similar()
                add_diff_to_list(diff, diffs)
                list_of_diffs.append(diffs)
        else:
            # this is the first commit
            diffs = []
            diff = commit.tree.diff_to_tree()
            add_diff_to_list(diff, diffs)
            list_of_diffs.append(diffs)

        entry.set_diff(list_of_diffs)

@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/log.ui")
class LogWindow(Adw.ApplicationWindow, DialogBase, PopoverBase, LogCalculator):
    """ log window """
    __gtype_name__ = "LogWindow"
    __gsignals__ = {
        'commit-selected': (GObject.SignalFlags.RUN_FIRST, GObject.TYPE_NONE, ()),
    }

    select_button = Gtk.Template.Child()
    content_box = Gtk.Template.Child()
    listview = Gtk.Template.Child()
    selection_model = Gtk.Template.Child()
    scrolled_window_commits = Gtk.Template.Child()

    show_all_branches_action = None

    commit_table = None

    current_hex = None
    current_branch = None
    branch_tag_dict = {}

    select_mode = False

    model = None

    selected_commit_hex = None
    last_selected_commit = 0

    hidden_remotes = []
    hide_local = False
    config_path = None

    def __init__(self, path, select_button_visible=False):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)
        PopoverBase.__init__(self)

        self.close_by_progress = False

        css_data = b"""
        columnview.graph-margin row cell:first-child {
            margin-top: -8px;
            margin-bottom: -8px;
        }
        """

        # override the cell margin so the graph lines go to the edge
        css = Gtk.CssProvider()
        try:
            css.load_from_data(css_data)
        except TypeError:
            # Older GTK4 bindings had the wrong introspection data.
            css.load_from_data(css_data.decode(), -1)
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.listview.add_css_class("graph-margin")

        self.select_button.set_visible(select_button_visible)
        self.select_mode = select_button_visible

        self.config_path = self.turtle.repo.path + "turtle_log"
        self.__read_config()

        self.connect("close-request", self._on_close_request)

        # settings menu action
        self.show_all_branches_action = Gio.SimpleAction.new_stateful(
            "show-all-branches",
            None,
            GLib.Variant.new_boolean(False))
        self.show_all_branches_action.connect("change-state", self._toggle_all_branches)
        self.add_action(self.show_all_branches_action)
        open_remotes_action = Gio.SimpleAction.new("branch-filter")
        open_remotes_action.connect("activate", self._open_branch_filter)
        self.add_action(open_remotes_action)

        # context menu actions
        self._add_action("action-pull-branch", self._pull_branch_from_popover)
        self._add_action("action-push-branch", self._push_branch_from_popover)
        self._add_action("action-checkout-reference", self._checkout_reference_from_popover)
        self._add_action("action-checkout-commit", self._checkout_commit_from_popover)
        self._add_action("action-merge-branch", self._merge_branch_from_popover)
        self._add_action("action-rebase-branch", self._rebase_branch_from_popover)
        self._add_action("action-create-branch-at", self._create_branch_at)
        self._add_action("action-create-tag-at", self._create_tag_at)
        self._add_action("action-delete-reference", self._delete_reference)
        self._add_action("action-reset", self._reset)

        self._set_title_repo()

        self.commit_table = CommitTable(self.turtle)
        self.commit_table.column_selected.set_visible(False)
        self.scrolled_window_commits.set_child(self.commit_table)

        self.model = LogListModel()
        self.selection_model.set_model(self.model)

        self.__refresh()

    def _on_close_request(self, _window):
        """ store settings on close """
        self.__write_config()

        return False

    def get_selected_commit(self):
        """ get the currently selected commit """
        selected = self.selection_model.get_selected()
        item = self.model.get_item(selected)
        return item

    def _toggle_all_branches(self, action, data):
        action.set_state(data)
        self.__refresh()

    def _open_branch_filter(self, _action, _data):
        remotes = self.turtle.get_remotes()
        hidden = LogFilter(remotes, self.hidden_remotes, self.hide_local)
        settings = QuickSettings("Remotes", "Filter branches by source", hidden, parent=self)
        settings.connect("response", self._open_branch_filter_response)
        settings.present()

    def _open_branch_filter_response(self, dialog, _response):
        hidden = dialog.get_extra_child()
        hidden_remotes, hide_local = hidden.get_hidden_remotes()

        if hidden_remotes != self.hidden_remotes or hide_local != self.hide_local:
            self.hide_local = hide_local
            self.hidden_remotes = hidden_remotes
            self.__refresh()

    def _pull_branch_from_popover(self, _widget, _data):
        self.model.set_items([])
        self._show_progress_window("Pulling", [self._do_pull, self._do_refresh], True)

    def _do_pull(self):
        message, title = self.turtle.pull(None, None, PullAction.FETCH_AND_MERGE)
        if message is not None:
            self._set_progress_message(title, message)

    def _push_branch_from_popover(self, _widget, _data):
        self.model.set_items([])
        self._show_progress_window("Pushing", [self._do_push, self._do_refresh], True)

    def _do_push(self):
        self.turtle.push(None, None)

    def _checkout_reference_from_popover(self, _widget, data):
        name = data.get_string()
        try:
            self.turtle.checkout(name=name)
            GLib.idle_add(self.__refresh)
        except Exception as ex:
            notification = Notification(str(ex), parent=self)
            notification.set_visible(True)

    def _checkout_commit_from_popover(self, _widget, data):
        name = data.get_string()
        try:
            self.turtle.checkout(name=name)
            GLib.idle_add(self.__refresh)
        except Exception as ex:
            notification = Notification(str(ex), parent=self)
            notification.set_visible(True)

    def _merge_branch_from_popover(self, _widget, data):
        name = data.get_string()
        try:
            message, title = self.turtle.merge(branch_name=name)
            notification = Notification(
                title="Merged" if title is None else title,
                message=f"Successfully merged {name}" if message is None else message,
                parent=self)
            notification.connect("response", lambda _, __: self.__refresh())
            notification.set_visible(True)
        except Exception as ex:
            notification = Notification(str(ex), parent=self)
            notification.set_visible(True)

    def _rebase_branch_from_popover(self, _widget, data):
        # TODO implement rebase from log
        _name = data.get_string()
        notification = Notification("rebase from log not implemented yet", parent=self)
        notification.set_visible(True)

    def _create_branch_at(self, _widget, data):
        # pylint: disable=C0415
        # avoid circular dependency
        from turtlevcs.dialogs.create_branch import CreateWindow
        # pylint: enable=C0415
        name = data.get_string()
        create_branch = CreateWindow(self.turtle.repo.workdir, commit=name)
        create_branch.set_transient_for(self)
        create_branch.set_modal(True)
        create_branch.connect("branch-or-tag-created", self._subdialog_finished)
        create_branch.set_visible(True)

    def _create_tag_at(self, _widget, data):
        # pylint: disable=C0415
        # avoid circular dependency
        from turtlevcs.dialogs.create_branch import CreateWindow, CreateType
        # pylint: enable=C0415
        name = data.get_string()
        create_tag = CreateWindow(
            self.turtle.repo.workdir,
            create_type=CreateType.TAG,
            commit=name)
        create_tag.set_transient_for(self)
        create_tag.set_modal(True)
        create_tag.connect("branch-or-tag-created", self._subdialog_finished)
        create_tag.set_visible(True)

    def _subdialog_finished(self, _widget):
        GLib.idle_add(self.__refresh)

    def _delete_reference(self, _widget, data):
        name = data.get_string()
        is_tag = name.startswith("refs/tags")
        short = name.split("/", 2)[-1]
        question = Question(
            f"Delete {'Tag' if is_tag else 'Branch'}?",
            message=f"The {'tag' if is_tag else 'branch'} '{short}' will be deleted.",
            callback=self.__do_delete_reference,
            data=name,
            parent=self)
        question.present()

    def _reset(self, _widget, data):
        # pylint: disable=C0415
        # avoid circular dependency
        from turtlevcs.dialogs.reset import ResetWindow
        # pylint: enable=C0415
        name = data.get_string()
        reset = ResetWindow(self.turtle.repo.workdir, commit=name)
        reset.set_transient_for(self)
        reset.set_modal(True)
        reset.connect("reset", self._subdialog_finished)
        reset.set_visible(True)

    def __do_delete_reference(self, response, data):
        if response:
            try:
                self.turtle.delete_reference(data)
            except Exception as ex:
                notification = Notification(str(ex), parent=self)
                notification.set_visible(True)
            GLib.idle_add(self.__refresh)

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__refresh()

    def __refresh(self):
        self.last_selected_commit = 0
        try:
            commit = self.model.get_item(self.selection_model.get_selected())
            self.selected_commit_hex = commit.hex
        except Exception as _ex:
            self.selected_commit_hex = None
        self.model.set_items([])
        self._show_progress_window("Loading", self._do_refresh, True)

    def __finish_update(self, model_list):
        self.model.set_items(model_list)

        # trigger selection changed handler manually once
        if self.last_selected_commit == self.selection_model.get_selected():
            self._log_selection_changed_handler(
                self.selection_model,
                self.last_selected_commit,
                None)
        else:
            self.selection_model.set_selected(self.last_selected_commit)
            try:
                self.listview.scroll_to(
                    self.last_selected_commit, None, Gtk.ListScrollFlags.NONE, None)
            except Exception as _ex:
                pass # scroll_to only available in gtk 4.12

        if self.progress.close_on_finish:
            self.progress.close()

    def _do_refresh(self):
        self._set_progress_message("Loading")
        self.current_hex = self.turtle.get_current_commit_hex()
        self.current_branch = self.turtle.get_current_branch_name()

        status, _ = self.turtle.get_commit_info(
            show_unversioned=True,
            show_ignored=False,
            amend=False)

        model_list = []

        if not self.select_mode:
            entry = LogListModelEntry(
                    short_id=None,
                    commit_hex=None,
                    message="Current working changes",
                    author=None,
                    date=None)
            diff_list = []
            for file in status:
                diff_list.append((
                    status[file],
                    None,
                    None,
                    file,
                    None))
            entry.set_diff([diff_list])
            model_list.append(entry)

        all_branches = self.show_all_branches_action.get_state()
        commit_list = self.turtle.log(
            all_branches=all_branches,
            ignored_remotes=self.hidden_remotes, hide_local=self.hide_local)
        self.branch_tag_dict = self.turtle.get_branch_commit_dictionary(
            self.hidden_remotes,
            self.hide_local and all_branches)
        self.branch_tag_dict = self.turtle.get_tag_commit_dictionary(self.branch_tag_dict)

        self.model.maximum = self.calculate_graph(commit_list, model_list)

        GLib.timeout_add(0, self.__finish_update, model_list)

    def __read_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        try:
            self.hidden_remotes = config["remotes"]["hidden"].split(",")
        except Exception as _ex:
            pass
        try:
            hide_local = config["remotes"]["hide_local"].lower() == "true"
            self.hide_local = hide_local
        except Exception as _ex:
            pass

    def __write_config(self):
        if len(self.hidden_remotes) > 0 or os.path.exists(self.config_path):
            config = configparser.ConfigParser()
            config["remotes"] = {}
            config["remotes"]["hidden"] = ",".join(self.hidden_remotes)
            config["remotes"]["hide_local"] = str(self.hide_local).lower()
            with open(self.config_path, "w", encoding="utf8") as config_file:
                config.write(config_file)


    @Gtk.Template.Callback()
    def _log_selection_changed_handler(self, _selection_model, _position, _data):
        item = self.get_selected_commit()
        if item is not None:
            if item.diff is None:
                self.calculate_diff_for_commit(item, self.turtle.repo.revparse_single(item.hex))
            self.commit_table.update_model_with_diff(item.diff, is_committed=item.hex is not None)

    @Gtk.Template.Callback()
    def _select_clicked(self, _widget):
        self.emit("commit-selected")

    @Gtk.Template.Callback()
    def _refresh_clicked(self, _widget):
        self.__refresh()

    @Gtk.Template.Callback()
    def _column_graph_setup_handler(self, _factory, listitem):
        area = Gtk.DrawingArea()
        listitem.set_child(area)

    @Gtk.Template.Callback()
    def _column_graph_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        area = listitem.get_child()

        def draw_me(_area, context, _width, height, entry):
            def set_color_to_context_by_index(index, context):
                (red, green, blue) = get_theme_colors()[index]
                f_red = red / 255
                f_green = green / 255
                f_blue = blue / 255
                context.set_source_rgb(f_red, f_green, f_blue)

            context.set_line_width(2)
            try:
                # draw graph lines
                i = 0
                for start, end, color_index in entry.old_lines:
                    set_color_to_context_by_index(color_index, context)
                    start_point = start * GRAPH_LINE_WIDTH + GRAPH_LINE_WIDTH / 2
                    end_point = end * GRAPH_LINE_WIDTH + GRAPH_LINE_WIDTH / 2
                    if start != end:
                        distance = end_point - start_point
                        start_point = start_point + distance / 2
                    context.move_to(start_point, 0)
                    context.line_to(end_point, height / 2)
                    context.stroke()
                    i += 1

                i = 0
                for start, end, color_index in entry.lines:
                    set_color_to_context_by_index(color_index, context)
                    start_point = start * GRAPH_LINE_WIDTH + GRAPH_LINE_WIDTH / 2
                    end_point = end * GRAPH_LINE_WIDTH + GRAPH_LINE_WIDTH / 2
                    if start != end:
                        distance = end_point - start_point
                        end_point = start_point + distance / 2
                    context.move_to(start_point, height / 2)
                    context.line_to(end_point, height)
                    context.stroke()
                    i += 1

                # draw node circle
                color_index = entry.color
                set_color_to_context_by_index(color_index, context)
                context.arc(
                    entry.node  * GRAPH_LINE_WIDTH + GRAPH_LINE_WIDTH / 2,
                    height / 2,
                    4,
                    0,
                    2 * math.pi)
                context.fill()
            except Exception as ex:
                print(f"exception: {str(ex)}")

        area.set_content_width(GRAPH_LINE_WIDTH * self.model.maximum)
        area.set_draw_func(draw_me, item)

    @Gtk.Template.Callback()
    def _column_hash_setup_handler(self, _factory, listitem):
        label = Gtk.Label()
        listitem.set_child(label)

    @Gtk.Template.Callback()
    def _column_hash_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        if item.short_id:
            label = listitem.get_child()
            if item.hex == self.current_hex:
                label.set_markup(f"<b>{item.short_id}</b>")
            else:
                label.set_label(item.short_id)

    @Gtk.Template.Callback()
    def _column_message_setup_handler(self, _factory, listitem):
        super_box = Gtk.Box()
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.HORIZONTAL)
        box.set_spacing(4)

        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        box.append(label)
        super_box.append(box)

        listitem.set_child(super_box)

    @Gtk.Template.Callback()
    def _column_message_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        super_box = listitem.get_child()
        box = super_box.get_first_child()
        tooltip = ""

        if item.message != item.message_full:
            tooltip += f"\"{item.message_full}\""

        if item.gpg_signature:
            tooltip += f"\n\n{item.gpg_signature}"

        if len(tooltip) > 0:
            box.set_tooltip_text(tooltip.strip())

        # remove all childs but the last one (contains the message)
        child = box.get_first_child()
        last_child = box.get_last_child()
        while child and child != last_child:
            box.remove(child)
            child = box.get_first_child()

        message = item.message

        def gesture_pressed_row(gesture, _n_press, _x, _y):
            super_box = gesture.get_widget()

            popover = None
            child = super_box.get_first_child()
            while child:
                if isinstance(child, Gtk.PopoverMenu):
                    popover = child
                    break
                child = child.get_next_sibling()

            if item.hex:
                self._create_popover(
                    super_box,
                    [
                        (f"Checkout {item.short_id}", "win.action-checkout-commit", item.hex),
                        (f"Create branch at {item.short_id}", "win.action-create-branch-at", item.hex),
                        (f"Create tag at {item.short_id}", "win.action-create-tag-at", item.hex),
                        (f"Reset to {item.short_id}", "win.action-reset", item.hex),
                    ],
                    popover)

        item.controller = self._add_popover_gesture(super_box, gesture_pressed_row)

        if item.hex in self.branch_tag_dict:
            for reference_name, name in self.branch_tag_dict[item.hex]:
                label_branch = Gtk.Label()
                if reference_name.startswith("refs/tags"):
                    color = get_theme_color_by_index(1)
                    ref = self.turtle.repo.revparse_single(reference_name)
                    if ref.type == pygit2.enums.ObjectType.TAG:
                        label_branch.set_tooltip_text(f"Annotation:\n{ref.message.strip()}")
                else:
                    color = get_theme_color_by_index(3 if name == self.current_branch else 0)
                reference_text = f"<span background=\"{color}\">{name}</span>"
                label_branch.set_markup(reference_text)
                label_branch.set_name(reference_name)

                def gesture_pressed_branch_or_tag(gesture, _n_press, _x, _y):
                    label = gesture.get_widget()
                    current_name = label.get_text()
                    current_reference_name = label.get_name()
                    is_tag = current_reference_name.startswith("refs/tags")

                    entries = []
                    if not is_tag and current_name == self.current_branch:
                        entries.append(
                            (f"Pull {current_name}", "win.action-pull-branch", current_name))
                        entries.append(
                            (f"Push {current_name}", "win.action-push-branch", current_name))

                    entries.extend(
                        [
                            (
                                f"Checkout {current_name}",
                                "win.action-checkout-reference",
                                current_reference_name),
                            (
                                f"Checkout {item.short_id}",
                                "win.action-checkout-commit",
                                item.hex),
                        ])

                    if not is_tag:
                        entries.extend(
                        [
                            (
                                f"Merge {current_name}",
                                "win.action-merge-branch",
                                current_reference_name),
                            (
                                f"Rebase onto {current_name}",
                                "win.action-rebase-branch",
                                current_reference_name),
                        ])

                    entries.extend(
                        [
                            (
                                f"Delete {current_name}",
                                "win.action-delete-reference",
                                current_reference_name),
                        ])

                    self._create_popover(label, entries)

                self._add_popover_gesture(label_branch, gesture_pressed_branch_or_tag)
                box.prepend(label_branch)

        if item.hex == self.current_hex:
            last_child.set_markup(f"<b>{message}</b>")
        else:
            last_child.set_label(message)

    @Gtk.Template.Callback()
    def _column_message_unbind_handler(self, _factory, listitem):
        item = listitem.get_item()
        super_box = listitem.get_child()

        if item.controller is not None:
            super_box.remove_controller(item.controller)
            item.controller = None

    @Gtk.Template.Callback()
    def _column_author_setup_handler(self, _factory, listitem):
        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        listitem.set_child(label)

    @Gtk.Template.Callback()
    def _column_author_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        if item.author:
            label = listitem.get_child()
            if item.hex == self.current_hex:
                label.set_markup(f"<b>{item.author}</b>")
            else:
                label.set_label(item.author)

    @Gtk.Template.Callback()
    def _column_date_setup_handler(self, _factory, listitem):
        label = Gtk.Label()
        listitem.set_child(label)

    @Gtk.Template.Callback()
    def _column_date_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        if item.date:
            label = listitem.get_child()
            if item.hex == self.current_hex:
                label.set_markup(f"<b>{item.date}</b>")
            else:
                label.set_label(item.date)

    @Gtk.Template.Callback()
    def _column_teardown_handler(self, _factory, listitem):
        listitem.set_child(None)

    @Gtk.Template.Callback()
    def _column_unbind_handler(self, _factory, listitem):
        label = listitem.get_child()
        if isinstance(label, Gtk.Label):
            label.set_label("")


if __name__ == "__main__":
    TurtleApp(LogWindow).run()
