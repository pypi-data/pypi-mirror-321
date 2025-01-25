""" submodules dialog

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
import pathlib
import gi
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.dialogs.base import DialogBase
from turtlevcs.dialogs import Notification

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, GLib


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/add_submodules.ui")
class AddSubmoduleDialog(Adw.MessageDialog):
    """ add submodule dialog """
    __gtype_name__ = "AddSubmoduleDialog"

    entry_repo = Gtk.Template.Child()
    entry_path = Gtk.Template.Child()

    open_dialog = None

    def __init__(self, parent, turtle):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        self.turtle = turtle

        self.set_heading("Add Submodule")

        self.entry_repo.connect("changed", self._update)
        self.entry_path.connect("changed", self._update)

        self.add_response("ok", "Ok")
        self.add_response("cancel", "Cancel")

        self._update()

    def _update(self, _widget=None):
        valid = (len(self.entry_repo.get_text()) > 0 and
            len(self.entry_path.get_text()) > 0 )

        self.set_response_enabled("ok", valid)

    def response(self, _dialog, _response):
        """ response """


@Gtk.Template(
    filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/remove_submodule.ui")
class RemoveSubmoduleDialog(Adw.MessageDialog):
    """ remove submodule dialog """
    __gtype_name__ = "RemoveSubmoduleDialog"

    complete_removal = Gtk.Template.Child()

    open_dialog = None
    name = None

    def __init__(self, parent, turtle, name):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        self.turtle = turtle
        self.name = name

        self.set_heading("Rmove Submodule")
        self.set_body(
            f"Do you want to remove the submoule '{name}'?\n"
            "NOTE: You might have to commit the change afterwards.")

        self.add_response("ok", "Ok")
        self.add_response("cancel", "Cancel")


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/submodules.ui")
class SubmodulesWindow(Adw.ApplicationWindow, DialogBase):
    """ show and edit submodules """
    __gtype_name__ = "SubmodulesWindow"

    add_button = Gtk.Template.Child()
    submodules = Gtk.Template.Child()
    checkbutton_init = Gtk.Template.Child()

    repo = None
    path = None

    submodule_selections = []

    def __init__(self, path):
        Adw.ApplicationWindow.__init__(self)
        DialogBase.__init__(self, path)

        self.close_by_progress = False

        self._set_title_repo()

        self.__update()

    def _add_callback(self, dialog, response):
        if response == "ok":
            try:
                self.repo = dialog.entry_repo.get_text()
                self.path = dialog.entry_path.get_text()
                self._show_progress_window("Adding", self._do_add)
            except Exception as ex:
                window = Notification(str(ex), title="Could not add submodule", parent=self)
                window.present()
                self.__update()

    def _do_add(self):
        title = "Done"
        message = f"Submodule '{self.path}' added."
        try:
            self.turtle.add_submodule(self.repo, self.path)
        except Exception as ex:
            title = "Failed"
            message = str(ex)

        self._set_progress_message(title, message)
        GLib.timeout_add(0, self.__update)

    def _delete_callback(self, dialog, response):
        if response == "ok":
            # remove from .git/modules if selected
            if dialog.complete_removal.get_active():
                try:
                    path = pathlib.Path(self.turtle.repo.path) / "modules" / dialog.name
                    shutil.rmtree(str(path))
                except Exception:
                    pass # ignore missing modules folder

            # remove from .gitmodules
            path = str(self.turtle.get_full_file_path(".gitmodules"))
            # config.read_file(path)
            gitmodules = open(path, "r", encoding="utf8")
            if gitmodules is not None:
                lines = gitmodules.readlines()
                new_lines = []
                is_current = False
                for line in lines:
                    if line.startswith("[submodule"):
                        trimmed = line.strip()
                        trimmed = trimmed.removeprefix("[submodule \"")
                        trimmed = trimmed.removesuffix("\"]")
                        is_current = trimmed == dialog.name

                    if not is_current:
                        new_lines.append(line)

                gitmodules.close()

            gitmodules = open(path, "w", encoding="utf8")
            if gitmodules is not None:
                gitmodules.writelines(new_lines)
                gitmodules.close()

            # remove folder from index
            try:
                self.turtle.remove_path(dialog.name)
            except Exception as _ex:
                pass # might not be added to index, so ignore exception

            # remove folder
            try:
                path = self.turtle.get_full_file_path(dialog.name)
                shutil.rmtree(str(path))
            except Exception:
                pass # ignore missing modules folder

        self.__update()

    def _on_cancel_clicked(self):
        self.close()

    def _on_refresh_clicked(self):
        self.__update()

    @Gtk.Template.Callback()
    def _add_clicked(self, _widget):
        dialog = AddSubmoduleDialog(self, self.turtle)
        dialog.connect("response", self._add_callback)
        dialog.present()

    @Gtk.Template.Callback()
    def _update_clicked(self, _widget):
        selected = []
        for path, checkbutton in self.submodule_selections:
            try:
                if checkbutton.get_active():
                    submodule = self.turtle.repo.lookup_submodule(path)
                    if submodule:
                        selected.append(path)
            except Exception:
                pass

        title = "Updated"
        message = "Succesfully updated submodule"
        if len(selected) > 1:
            message += "s"

        try:
            init = self.checkbutton_init.get_active()
            self.turtle.repo.update_submodules(selected, init)
        except Exception as ex:
            title = "Failed"
            message = str(ex)

        window = Notification(message, title=title, parent=self)
        window.present()

    def __delete_clicked(self, widget):
        name = widget.get_name()

        dialog = RemoveSubmoduleDialog(self, self.turtle, name)
        dialog.connect("response", self._delete_callback)
        dialog.present()

    def __update(self, _quick=False):
        self.add_button.set_sensitive(False)

        child = self.submodules.get_first_child()
        while child:
            self.submodules.remove(child)
            child = self.submodules.get_first_child()

        submodules = self.turtle.get_submodules()
        self.submodule_selections = []

        for name in submodules:
            valid = True
            submodule = self.turtle.repo.lookup_submodule(name)
            row = Adw.ActionRow()
            row.set_selectable(False)
            checkbutton = Gtk.CheckButton()
            try:
                row.set_title(submodule.path)
                self.submodule_selections.append((submodule.path, checkbutton))
            except Exception:
                row.set_title("[invalid submodule path]")
                valid = False
            try:
                row.set_subtitle(submodule.url)
            except Exception:
                row.set_subtitle("[invalid submodule url]")
                valid = False
            checkbutton.set_sensitive(valid)
            checkbutton.set_active(valid)
            row.add_prefix(checkbutton)
            button_remove = Gtk.Button()
            button_remove.set_valign(Gtk.Align.CENTER)
            button_remove.set_name(name)
            button_remove.set_icon_name("edit-delete-symbolic")
            button_remove.connect("clicked", self.__delete_clicked)
            row.add_suffix(button_remove)
            self.submodules.append(row)

        if len(submodules) == 0:
            row = Adw.ActionRow()
            row.set_selectable(False)
            row.set_title("No submodules available")
            row.set_subtitle("You can add a submodules if you want")
            self.submodules.append(row)

        self.add_button.set_sensitive(True)


if __name__ == "__main__":
    TurtleApp(SubmodulesWindow).run()
