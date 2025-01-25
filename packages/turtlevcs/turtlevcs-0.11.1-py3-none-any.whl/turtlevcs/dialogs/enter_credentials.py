""" enter credentials dialog

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
import turtlevcs
from turtlevcs.turtle_app import TurtleApp
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk, GLib, Gio


@Gtk.Template(
    filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/enter_credentials.ui")
class EnterCredentials(Adw.MessageDialog):
    """ credentials dialog """
    __gtype_name__ = "EnterCredentials"

    ok = False
    key = None

    condition = None
    allowed_types = None

    label_user = Gtk.Template.Child()
    label_password = Gtk.Template.Child()
    entry_user = Gtk.Template.Child()
    entry_password = Gtk.Template.Child()
    store_password = Gtk.Template.Child()

    def __init__(
            self,
            parent=None,
            url=None,
            username_from_url=None,
            condition=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        self.condition = condition

        self.set_body(
            "Please enter your credentials" +
            (f" for\n{url}" if url is not None else ""))

        settings = turtlevcs.get_settings()
        if turtlevcs.can_store_password() and settings.get_boolean("enable-store-passwords"):
            self.store_password.set_active(settings.get_boolean("credentials-store-password"))
        else:
            self.store_password.set_visible(False)

        self.entry_user.set_text(username_from_url if username_from_url is not None else "")

        self.entry_user.connect("changed", self._update)
        self.entry_password.connect("changed", self._update)

        self.add_response("ok", "Ok")
        self.add_response("cancel", "Cancel")

        self.connect("response", self.response)

        self._update()

        GLib.timeout_add(0, self.present)

    def _update(self, _widget=None):
        valid = self.entry_password.get_text() != "" and self.entry_user.get_text() != ""
        self.set_response_enabled("ok", valid)

    def get_credentials(self):
        """ get user credentials """
        if self.ok:
            return (
                self.entry_user.get_text(),
                self.entry_password.get_text(),
                self.store_password.get_active())

        raise RuntimeError("No credentials provided")

    def response(self, _dialog, response):
        """ response """
        self.ok = response == "ok"
        if self.condition is not None:
            with self.condition:
                self.condition.notify()

if __name__ == "__main__":
    TurtleApp(EnterCredentials).run()
