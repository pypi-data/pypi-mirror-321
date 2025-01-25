""" remotes dialog

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
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs import Question, Notification

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/remotes_dialog.ui")
class RemoteDialog(Adw.MessageDialog):
    """ remote add or edit dialog """
    __gtype_name__ = "RemoteDialog"

    entry_name = Gtk.Template.Child()
    entry_fetch = Gtk.Template.Child()
    entry_push = Gtk.Template.Child()

    name = None
    fetch = None
    push = None

    def __init__(self, parent, heading=None, name=None, fetch=None, push=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        if heading:
            self.set_heading(heading)

        self.name = name
        if name:
            self.entry_name.set_text(name)

        self.fetch = fetch
        if fetch:
            self.entry_fetch.set_text(fetch)

        self.push = push
        if push:
            self.entry_push.set_text(push)

        self.entry_name.connect("changed", self._update)
        self.entry_fetch.connect("changed", self._update)

        self.add_response("ok", "Ok")
        self.add_response("cancel", "Cancel")

        self._update()

    def _update(self, _widget=None):
        valid = (len(self.entry_name.get_text()) > 0 and
            len(self.entry_fetch.get_text()) > 0 )

        self.set_response_enabled("ok", valid)

@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/remotes.ui")
class RemotesWindow(Adw.ApplicationWindow, DialogBase):
    """ show and edit remotes """
    __gtype_name__ = "RemotesWindow"

    add_button = Gtk.Template.Child()
    remotes = Gtk.Template.Child()

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)

        self._set_title_repo()

        self.__update()

    def _add_callback(self, dialog, response):
        if response == "ok":
            try:
                name = dialog.entry_name.get_text()
                url = dialog.entry_fetch.get_text()
                push_url = dialog.entry_push.get_text()
                self.turtle.update_remote(None, name, url, push_url)
            except Exception as ex:
                window = Notification(str(ex), title="Could not add remote", parent=self)
                window.present()

        self.__update()

    def _edit_callback(self, dialog, response):
        if response == "ok":
            try:
                old_name = dialog.name
                name = dialog.entry_name.get_text()
                url = dialog.entry_fetch.get_text()
                push_url = dialog.entry_push.get_text()
                self.turtle.update_remote(old_name, name, url, push_url)
            except Exception as ex:
                window = Notification(str(ex), title="Could not edit remote", parent=self)
                window.present()

        self.__update()

    def _delete_callback(self, response, name):
        if response:
            try:
                self.turtle.remove_remote(name)
            except Exception as ex:
                window = Notification(str(ex), title="Could not delete remote", parent=self)
                window.present()

        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    @Gtk.Template.Callback()
    def _add_clicked(self, _widget):
        dialog = RemoteDialog(self, "Add Remote")
        dialog.connect("response", self._add_callback)
        dialog.present()

    def __edit_clicked(self, widget):
        name = widget.get_name()
        fetch, push = self.turtle.get_remote_url_by_name(name)
        dialog = RemoteDialog(self, "Modify Remote", name, fetch, push)
        dialog.connect("response", self._edit_callback)
        dialog.present()

    def __delete_clicked(self, widget):
        name = widget.get_name()

        question = Question(
                "Delete Remote?",
                message=f"The remote '{name}' will be deleted.",
                callback=self._delete_callback,
                data=name,
                parent=self)
        question.present()

    def __update(self):
        self.add_button.set_sensitive(False)

        child = self.remotes.get_first_child()
        while child:
            self.remotes.remove(child)
            child = self.remotes.get_first_child()

        remotes = self.turtle.get_remotes()

        for remote in remotes:
            row = Adw.ActionRow()
            row.set_selectable(False)
            row.set_title(remote.name)
            row.set_subtitle(remote.url)
            button_edit = Gtk.Button()
            button_edit.set_valign(Gtk.Align.CENTER)
            button_edit.set_name(remote.name)
            button_edit.set_icon_name("document-edit-symbolic")
            button_edit.connect("clicked", self.__edit_clicked)
            row.add_suffix(button_edit)
            button_remove = Gtk.Button()
            button_remove.set_valign(Gtk.Align.CENTER)
            button_remove.set_name(remote.name)
            button_remove.set_icon_name("edit-delete-symbolic")
            button_remove.connect("clicked", self.__delete_clicked)
            row.add_suffix(button_remove)
            self.remotes.append(row)

        if len(remotes) == 0:
            row = Adw.ActionRow()
            row.set_selectable(False)
            row.set_title("No remotes available")
            row.set_subtitle("You can add a remote if you want")
            self.remotes.append(row)

        self.add_button.set_sensitive(True)


if __name__ == "__main__":
    TurtleApp(RemotesWindow).run()
