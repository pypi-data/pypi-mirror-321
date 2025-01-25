""" references dialog

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
from turtlevcs.dialogs.base import DialogBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gdk, Gio, GLib, GObject


class ReferenceListModelEntry(GObject.Object):
    """ an entry in the references model, which represents a single reference """

    name = None

    def __init__(self, name):
        GObject.Object.__init__(self)
        self.name = name

        self.is_local_branch = self.name.startswith("refs/heads/")
        self.is_remote_branch = self.name.startswith("refs/remotes/")
        self.is_tag = self.name.startswith("refs/tags/")


class ReferenceListModel(GObject.Object, Gio.ListModel):
    """ reference model, contains references """

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
        return type(ReferenceListModelEntry)

    def do_get_n_items(self):
        """ get model item list length """
        return len(self.items)

    def set_items(self, items):
        """ update model items """
        old_length = len(self.items)
        self.items = items
        self.items_changed(0, old_length, len(self.items))


class ReferencesFilter(Gtk.Filter):
    """ references filter """

    show_local_branches = True
    show_remote_branches = True
    show_tags = True

    def __init__(self):
        Gtk.Filter.__init__(self)

    def do_match(self, item):
        """ filter model items """
        local = self.show_local_branches and item.is_local_branch
        remote = self.show_remote_branches and item.is_remote_branch
        tag = self.show_tags and item.is_tag

        return local or remote or tag


@Gtk.Template(
    filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/reference_details.ui")
class ReferenceDetailsDialog(Adw.MessageDialog):
    """ reference details dialog """
    __gtype_name__ = "ReferenceDetailsDialog"

    label_name = Gtk.Template.Child()
    label_full_name = Gtk.Template.Child()
    label_type = Gtk.Template.Child()
    label_short_id = Gtk.Template.Child()
    row_annotation = Gtk.Template.Child()
    label_annotation = Gtk.Template.Child()

    def __init__(self, parent, name, turtle):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        ref = turtle.repo.references[name]
        ref_object = turtle.repo.revparse_single(name)
        annotation = None

        if name.startswith("refs/heads/"):
            ref_type = "local branch"
        elif name.startswith("refs/remotes/"):
            ref_type = "remote branch"
        elif name.startswith("refs/tags/"):
            if ref_object.type == pygit2.enums.ObjectType.TAG:
                ref_type = "annotated tag"
                annotation = ref_object.message
            else:
                ref_type = "tag"
        else:
            ref_type = "unknown"

        self.label_name.set_label(ref.shorthand)
        self.label_full_name.set_label(ref.name)
        self.label_type.set_label(ref_type)
        self.label_short_id.set_label(ref_object.short_id)

        if annotation is not None:
            self.label_annotation.set_label(annotation.strip())
        else:
            self.row_annotation.set_visible(False)

        self.add_response("ok", "Ok")

    @Gtk.Template.Callback()
    def _short_id_clicked(self, _widget):
        clipboard = Gdk.Display().get_default().get_clipboard()
        short_id = self.label_short_id.get_label()
        clipboard.set(short_id)


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/references.ui")
class ReferencesWindow(Adw.ApplicationWindow, DialogBase):
    """ references dialog """
    __gtype_name__ = "ReferencesWindow"

    model = ReferenceListModel()
    filter_model = Gtk.FilterListModel()

    refresh_button = Gtk.Template.Child()

    scrolled_window = Gtk.Template.Child()
    references_view = Gtk.Template.Child()
    selection_model = Gtk.Template.Child()

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)

        self._set_title_repo()

        self.filter = ReferencesFilter()
        self.filter_model.set_filter(self.filter)
        self.filter_model.set_model(self.model)
        self.selection_model.set_model(self.filter_model)

        # settings menu action
        def add_action(action_name, function):
            action = Gio.SimpleAction.new_stateful(
                action_name,
                None,
                GLib.Variant.new_boolean(True))
            action.connect("change-state", function)
            self.add_action(action)

            return action

        self.local_branches_action = add_action("show-local-branches", self._toggle_filter)
        self.remote_branches_action = add_action("show-remote-branches", self._toggle_filter)
        self.tags_action = add_action("show-tags", self._toggle_filter)

        self.__refresh()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__refresh()

    def _toggle_filter(self, action, data):
        action.set_state(data)

        self.filter.show_local_branches = self.local_branches_action.get_state().get_boolean()
        self.filter.show_remote_branches = self.remote_branches_action.get_state().get_boolean()
        self.filter.show_tags = self.tags_action.get_state().get_boolean()
        self.filter.emit("changed", Gtk.FilterChange.DIFFERENT)

    def __refresh(self):
        self.refresh_button.set_sensitive(False)

        refs = []
        for ref in self.turtle.get_list_of_references():
            refs.append(ReferenceListModelEntry(ref))

        self.model.set_items(refs)

        self.refresh_button.set_sensitive(True)

    @Gtk.Template.Callback()
    def _refresh_clicked(self, widget):
        self.__refresh()

    @Gtk.Template.Callback()
    def _listview_activated_handler(self, _widget, position):
        ref = self.filter_model.get_item(position)
        details = ReferenceDetailsDialog(self, ref.name, self.turtle)
        details.present()

    @Gtk.Template.Callback()
    def _column_name_setup_handler(self, _factory, listitem):
        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        listitem.set_child(label)

    @Gtk.Template.Callback()
    def _column_name_teardown_handler(self, _factory, listitem):
        pass

    @Gtk.Template.Callback()
    def _column_name_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        label = listitem.get_child()

        label.set_label(item.name)

    @Gtk.Template.Callback()
    def _column_name_unbind_handler(self, _factory, listitem):
        pass


if __name__ == "__main__":
    TurtleApp(ReferencesWindow).run()
