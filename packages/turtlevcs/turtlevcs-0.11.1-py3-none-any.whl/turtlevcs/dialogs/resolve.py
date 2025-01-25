""" resolve dialog

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
import shutil
import gi
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs import Question, Subprocess
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs.commit import CommitWindow

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gio, GObject



class ResolveListModelEntry(GObject.Object):
    """ an entry in the resolve model, which represents a single conflicted file """
    base = None
    ours = None
    theirs = None
    selected = False

    def __init__(self, base, ours, theirs):
        GObject.Object.__init__(self)
        self.base = base
        self.ours = ours
        self.theirs = theirs


class ResolveListModel(Gio.ListStore):
    """ resolve model, contains conflicted files """

    def __init__(self):
        Gio.ListStore.__init__(self)

@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/resolve_method.ui")
class ResolveMethodDialog(Adw.MessageDialog):
    """ resolve method dialog """
    __gtype_name__ = "ResolveMethodDialog"

    entry_theirs = Gtk.Template.Child()
    entry_ours = Gtk.Template.Child()
    entry_current = Gtk.Template.Child()
    button_theirs = Gtk.Template.Child()
    button_ours = Gtk.Template.Child()
    button_current = Gtk.Template.Child()
    button_triple = Gtk.Template.Child()

    turtle = None

    item = None

    def __init__(self, parent, turtle, item):
        Adw.MessageDialog.__init__(self, transient_for=parent)
        self.turtle = turtle
        self.item = item
        name = item.base.path if item.base else item.ours.path

        self.set_body(f"Choose how to resolve '{name}'.")

        self.entry_theirs.set_subtitle(item.theirs.hex)
        self.entry_ours.set_subtitle(item.ours.hex)
        self.entry_current.set_subtitle("Conflicted File")

        self.add_response("ours", "Ours")
        self.add_response("theirs", "Theirs")
        self.add_response("as-is", "As Is")
        self.add_response("cancel", "Cancel")

    @Gtk.Template.Callback()
    def _show_file_button_clicked(self, button):
        file1 = None
        file2 = None
        name = self.item.base.path if self.item.base else self.item.ours.path
        base_file = self.turtle.get_files_from_index(self.item.base, "base")
        file_ours = self.turtle.get_files_from_index(self.item.ours, "ours")
        file_theirs = self.turtle.get_files_from_index(self.item.theirs, "theirs")
        filename_local = self.turtle.repo.workdir + name

        if button is self.button_ours:
            subprocess = Subprocess(["meld", base_file.name, file_ours.name], self)
            file1 = base_file
            file2 = file_ours
        elif button is self.button_theirs:
            subprocess = Subprocess(["meld", base_file.name, file_theirs.name], self)
            file1 = base_file
            file2 = file_theirs
        elif button is self.button_triple:
            subprocess = Subprocess(
                ["meld", file_ours.name, filename_local, file_theirs.name], self)
            file1 = file_ours
            file2 = file_theirs
        else:
            subprocess = Subprocess(["gnome-text-editor", filename_local], self)

        # store temp file objects in dialog to keep them alive
        subprocess.temp_file1 = file1
        subprocess.temp_file2 = file2

        subprocess.present()

@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/resolve.ui")
class ResolveWindow(Adw.ApplicationWindow, DialogBase):
    """ resolve dialog """
    __gtype_name__ = "ResolveWindow"

    merge_info = Gtk.Template.Child()
    merge_info_row = Gtk.Template.Child()
    abort_button = Gtk.Template.Child()
    merge_button = Gtk.Template.Child()
    selection_model = Gtk.Template.Child()

    model = None
    original_message = ""

    file_resolve = None

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)

        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    def __update(self):
        # reload turtle repository to detect conflicts properly
        self.turtle.reload()

        self.model = ResolveListModel()
        self.selection_model.set_model(self.model)

        is_merge, merge_head = self.turtle.is_merge_in_progress()
        is_rebase, rebase_head = self.turtle.is_rebase_in_progress()

        if is_merge:
            self.merge_info_row.set_title("Currently merging")
            self.merge_info_row.set_subtitle(f"{merge_head} into HEAD")
        elif is_rebase:
            self.merge_info_row.set_title("Currently rebasing")
            self.merge_info_row.set_subtitle(f"Rebase HEAD: {rebase_head}")
        else:
            self.merge_info_row.set_title("Not merging or rebasing")
            self.merge_info_row.set_subtitle("Currently no merge or rebase in progress")

        conflicts = self.turtle.get_conflicts()
        for base, ours, theirs in conflicts:
            self.model.append(ResolveListModelEntry(base, ours, theirs))

        conflicted = len(conflicts) > 0

        self.merge_button.set_sensitive(not conflicted)

        self.merge_button.set_visible(is_merge)
        self.abort_button.set_visible(is_merge)
        self.abort_button.set_visible(False) # TODO abort not possible atm

    def _open_resolve_editor(self, item):
        file_ours = self.turtle.get_files_from_index(item.ours, "ours")
        file_theirs = self.turtle.get_files_from_index(item.theirs, "theirs")
        name = item.base.path if item.base else item.ours.path

        subprocess = Subprocess([
                "meld",
                file_ours.name,
                self.turtle.repo.workdir + name,
                file_theirs.name,
                "--output",
                self.turtle.repo.workdir + name
            ],
            self)
        # store temp file objects in dialog to keep them alive
        subprocess.temp_file1 = file_ours
        subprocess.temp_file2 = file_theirs
        subprocess.item = item

        subprocess.connect("response", self._open_resolve_editor_callback)
        subprocess.present()

    def _open_resolve_editor_callback(self, dialog, _response):
        item = dialog.item
        name = item.base.path if item.base else item.ours.path
        question = Question(
            "Resolve",
            message=f"Mark '{name}' as resolved?",
            callback=self._mark_as_resolved,
            data=name,
            parent=self)
        question.present()

    def _mark_as_resolved(self, response, path, from_other_source=False):
        if response:
            if from_other_source:
                shutil.copyfile(self.file_resolve.name, self.turtle.repo.workdir + path)
            self.turtle.stage_file(path)
        self.__update()

    def _choose_resolve_button_clicked(self, button):
        position = int(button.get_name())
        item = self.model.get_item(position)
        dialog = ResolveMethodDialog(self, self.turtle, item)
        dialog.connect("response", self._on_response)
        dialog.present()

    def _on_response(self, widget, response):
        mark_resolved = False
        from_other_source = False
        if response == "as-is":
            self.file_resolve = None # reset possible file_resolve object
            mark_resolved = True
        elif response == "ours":
            self.file_resolve = self.turtle.get_files_from_index(widget.item.ours, "ours")
            from_other_source = True
            mark_resolved = True
        elif response == "theirs":
            self.file_resolve = self.turtle.get_files_from_index(widget.item.theirs, "theirs")
            from_other_source = True
            mark_resolved = True

        if mark_resolved:
            name = widget.item.base.path if widget.item.base else widget.item.ours.path
            self._mark_as_resolved(True, name, from_other_source)

    @Gtk.Template.Callback()
    def _refresh_clicked(self, __widget):
        self.__update()

    @Gtk.Template.Callback()
    def _abort_button_handler(self, __widget):
        pass # TODO abort not possible atm

    @Gtk.Template.Callback()
    def _merge_button_handler(self, __widget):
        commit_window = CommitWindow(self.turtle.repo.workdir)
        self.show_new_window(commit_window)

    @Gtk.Template.Callback()
    def _listview_activated_handler(self, __widget, position):
        item = self.model.get_item(position)
        self._open_resolve_editor(item)

    @Gtk.Template.Callback()
    def _column_path_setup_handler(self, __factory, listitem):
        box = Gtk.Box()
        label = Gtk.Label()
        label.set_hexpand(True)
        label.set_halign(Gtk.Align.START)

        button = Gtk.Button()
        button.set_icon_name("edit-paste-symbolic")
        button.set_halign(Gtk.Align.END)

        box.append(label)
        box.append(button)
        listitem.set_child(box)

    @Gtk.Template.Callback()
    def _column_path_teardown_handler(self, __factory, listitem):
        listitem.set_child(None)

    @Gtk.Template.Callback()
    def _column_path_bind_handler(self, __factory, listitem):
        item = listitem.get_item()
        _, position = self.model.find(item)
        box = listitem.get_child()
        label = box.get_first_child()
        name = item.base.path if item.base else item.ours.path
        label.set_label(name)

        button = box.get_last_child()
        button.set_name(str(position))
        button.connect("clicked", self._choose_resolve_button_clicked)


if __name__ == "__main__":
    TurtleApp(ResolveWindow).run()
