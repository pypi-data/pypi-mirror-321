""" collection of base classes

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
import pathlib
import gi
from turtlevcs.turtle import TurtleBase, PullAction, CreateFrom
from turtlevcs.dialogs.push_table import PushTable
from turtlevcs.dialogs import Progress
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, Gio, GLib


class DialogBase(TurtleBase):
    """ dialog base class, implements key event handlers """
    app = None
    progress = None
    close_by_progress = True

    file_list = None # file list as parameter, currently used for commit window

    updating_model_from_signal = False

    def __init__(self, path, no_turtle=False):
        # path can be list of paths to preselect files to commit
        if "," in path:
            self.file_list = path.split(",")
            path = self.file_list[0]
        else:
            self.file_list = [path]

        TurtleBase.__init__(self, path, no_turtle)

        if no_turtle is False and self.file_list is not None:
            file_list_trimmed = []
            for f in self.file_list:
                if pathlib.Path(f).is_file():
                    path = self.turtle.get_relative_file_path(f)
                    file_list_trimmed.append(path)
            self.file_list = file_list_trimmed

        self.connect("show", self._on_show)

        if isinstance(self, Gtk.ApplicationWindow):
            keycontroller = Gtk.EventControllerKey()
            keycontroller.connect("key-pressed", self._key_press_event)
            keycontroller.connect("key-released", self._key_release_event)
            self.add_controller(keycontroller)

    def _ok_clicked(self, widget):
        pass

    def _cancel_clicked(self, widget):
        pass

    def _refresh_clicked(self, widget):
        pass

    def _on_show(self, _widget):
        # save the current application here
        # get_application might return None (i.e. in response callback of message dilaog)
        self.app = self.get_application()

    def _key_press_event(self, _controller, keyval, _keycode, state):
        if keyval == Gdk.KEY_Escape:
            self._on_cancel_clicked()

        if keyval == Gdk.KEY_F5:
            self._on_refresh_clicked()

        if (state & Gdk.ModifierType.CONTROL_MASK
                and keyval == Gdk.KEY_w):
            self._on_cancel_clicked()

        if (state & Gdk.ModifierType.CONTROL_MASK
                and keyval == Gdk.KEY_q):
            self._on_cancel_clicked()

        if (state & Gdk.ModifierType.CONTROL_MASK
                and keyval == Gdk.KEY_r):
            self._on_refresh_clicked()

    def _key_release_event(self, controller, keyval, keycode, state):
        pass

    def show_new_window(self, window, close=True):
        """ show a new window and optionally close this one """
        window.present()

        if self.app is not None:
            self.app.add_window(window)

        if close:
            self.close()

    def _show_progress_window(self, message, function, close_on_finish=False):
        self.progress = Progress(message, function, self)
        self.progress.connect("response", self._on_close_by_progress)
        self.progress.close_on_finish = close_on_finish
        self.progress.set_visible(True)

    def _update_progress_message(self, message):
        if self.progress:
            GLib.timeout_add(0, self._set_progress_message, None, message)

    def _set_progress_message(self, message, details=None):
        if self.progress is not None:
            if message is not None:
                self.progress.set_heading(message)
            if details is not None:
                self.progress.set_body(details)

    def _on_close_by_progress(self, _widget, _response):
        if self.close_by_progress:
            self.close()

    def _set_title_repo(self, prefix=None):
        repo_name = self.turtle.get_repo_name()
        title = ""
        if prefix is not None and len(prefix) > 0:
            title = prefix + " - "

        title = title + f"repo: {repo_name}"
        self.set_title(title)

    def _set_title_branch(self):
        branch_name = self.turtle.get_current_branch_name()
        self.set_title(f"branch: {branch_name}")

    def _add_action(self, name, callback):
        action = Gio.SimpleAction.new(name, GLib.VariantType.new("s"))
        action.connect("activate", callback)
        self.add_action(action)

    def _fill_branch_data(self, prefer_origin=False):
        current_remote, current_branch, local_branches, remotes = self.turtle.get_push_info()

        if not self.updating_model_from_signal:
            index = 0
            i = 0
            current = self.branch.get_selected_item()
            if current:
                index = self.branch.get_selected()
            else:
                while self.branch_model.get_n_items() > 0:
                    self.branch_model.remove(0)
                for branch in local_branches:
                    if branch == current_branch:
                        index = i
                    self.branch_model.append(branch)
                    i += 1

            self.branch.set_selected(index)

            index = 0
            i = 0
            index_origin = 0
            current = self.upstream.get_selected_item()
            if current:
                index = self.upstream.get_selected()
            else:
                # only update model on first call
                while self.upstream_model.get_n_items() > 0:
                    self.upstream_model.remove(0)

                for remote in remotes:
                    if current_remote is None:
                        if prefer_origin and remote.name == "origin":
                            index_origin = i
                    if remote.name == current_remote:
                        index = i

                    self.upstream_model.append(remote.name)
                    i += 1

            self.upstream.set_selected(index_origin if current_remote is None else index)

    def _get_selected_branch_and_upstream_names(self):
        try:
            branch_name = self.branch.get_selected_item().get_string()
        except Exception:
            branch_name = None
        try:
            remote_name = self.upstream.get_selected_item().get_string()
        except Exception:
            remote_name = None

        return branch_name, remote_name


class PushBase():
    """ push base class, needs DialogBase as a sibling and provides a PushWidget """

    branch_name = None
    remote_name = None

    def __init__(self):
        self.push_table = PushTable(self.turtle)

    def _push(self):
        self.branch_name, self.remote_name = self._get_selected_branch_and_upstream_names()

        self._show_progress_window("Pushing branch", self._do_push)

    def _do_push(self):
        try:
            self.turtle.push(self.branch_name, self.remote_name)
            title = "Pushed"
            summary = "Successfully pushed branch."
        except Exception as ex:
            title = "Push Failed"
            summary = str(ex)

        self._set_progress_message(title, details=summary)

    def _branch_or_upstream_changed(self):
        if not self.is_updating:
            branch_name, remote_name = self._get_selected_branch_and_upstream_names()
            self.push_table.update_commits(branch_name, remote_name)


class PullBase():
    """ pull base class, needs DialogBase as a sibling """

    branch_name = None
    remote_name = None
    pull_action = PullAction.FETCH_AND_MERGE

    def __init__(self):
        pass

    def _pull(self, pull_action):
        self.pull_action = pull_action
        self.branch_name, self.remote_name = self._get_selected_branch_and_upstream_names()

        self._show_progress_window("Updating branch", self._do_pull)

    def _do_pull(self):
        try:
            message, title = self.turtle.pull(self.branch_name, self.remote_name, self.pull_action)

            if title is None:
                title = "Updated"
            if message is None:
                message = "Successfully updated branch."
        except Exception as ex:
            title = "Update Failed"
            message = f"{str(ex)}"

        self._set_progress_message(title, details=message)

    def _branch_or_upstream_changed(self):
        if not self.is_updating:
            branch_name, remote_name = self._get_selected_branch_and_upstream_names()
            self.push_table.update_commits(branch_name, remote_name)

class PopoverBase():
    """ popover base class """

    def __init__(self):
        pass

    def _add_popover_gesture(self, widget, callback):
        gesture = Gtk.GestureClick()
        gesture.connect("pressed", callback)
        gesture.set_button(3)
        widget.add_controller(gesture)

        return gesture

    def _create_popover(self, parent, entries, popover=None):
        if len(entries) < 1:
            return

        if not popover:
            popover = Gtk.PopoverMenu()
            popover.set_parent(parent)
        menu = Gio.Menu()

        for text, action, target in entries:
            # escape underline, gtk uses it for menu item shortcut
            item = Gio.MenuItem.new(text.replace("_", "__"), action)
            if target and isinstance(target, str):
                item.set_attribute_value("target", GLib.Variant("s", target))
            menu.append_item(item)

        popover.set_menu_model(menu)
        popover.popup()


class BasedOnBase():
    """ based on base class """

    source = CreateFrom.HEAD
    source2 = CreateFrom.HEAD

    with_working_copy = False

    def __init__(self, with_working_copy=False):
        self.with_working_copy = with_working_copy

    def _based_on_changed(self, second_source=False):
        is_head = False
        if second_source:
            is_branch = self.branch_button2.get_active()
            is_commit = self.commit_button2.get_active()
            self.branch_row2.set_visible(is_branch)
            self.commit_row2.set_visible(is_commit)
        else:
            is_branch = self.branch_button.get_active()
            is_commit = self.commit_button.get_active()
            self.branch_row.set_visible(is_branch)
            self.commit_row.set_visible(is_commit)

        try:
            # head option might not be available
            if second_source:
                is_head = self.head_button2.get_active()
                self.head_row2.set_visible(is_head)
            else:
                is_head = self.head_button.get_active()
                self.head_row.set_visible(is_head)
        except Exception:
            pass

        source = CreateFrom.HEAD
        if is_head:
            source = CreateFrom.HEAD
        elif is_branch:
            source = CreateFrom.BRANCH
        elif is_commit:
            source = CreateFrom.COMMIT
        elif self.with_working_copy:
            source = CreateFrom.WORKING_COPY

        if second_source:
            self.source2 = source
        else:
            self.source = source

    def _is_based_on_valid(self, second_source=False):
        if second_source:
            commit_valid = \
                not self.commit_button2.get_active() or len(self.commit_row2.get_text()) > 0
            branch_valid = \
                not self.branch_button2.get_active() or self.branch_row2.get_selected_item()
        else:
            commit_valid = \
                not self.commit_button.get_active() or len(self.commit_row.get_text()) > 0
            branch_valid = \
                not self.branch_button.get_active() or self.branch_row.get_selected_item()

        return commit_valid and branch_valid

    def _get_base(self):
        if self.source is CreateFrom.HEAD:
            return self.turtle.get_current_commit_hex()
        elif self.source is CreateFrom.BRANCH:
            return self.branch_row.get_selected_item().get_string()
        else:
            return self.commit_row.get_text()

    def _get_base_revision(self, second_source=False):
        revision = None
        source = self.source2 if second_source else self.source

        if source is CreateFrom.HEAD:
            commit_hex = self.turtle.get_current_commit_hex()
            revision = self.turtle.get_revision_by_commit(commit_hex)
        elif source is CreateFrom.BRANCH:
            if second_source:
                branch_name =  self.branch_row2.get_selected_item().get_string()
            else:
                branch_name =  self.branch_row.get_selected_item().get_string()
            revision = self.turtle.get_revision_by_branch(branch_name)
        elif source is CreateFrom.COMMIT:
            commit_hex = \
                self.commit_row2.get_text() if second_source else self.commit_row.get_text()
            revision = self.turtle.get_revision_by_commit(commit_hex)

        return revision
