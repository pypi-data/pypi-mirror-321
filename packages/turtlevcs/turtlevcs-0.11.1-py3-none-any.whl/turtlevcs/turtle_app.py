""" turtle app

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
import traceback
from sys import argv
import gi
import turtlevcs
from turtlevcs.dialogs import Notification
from turtlevcs.dialogs.base import DialogBase
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gdk, Gio


class TurtleApp(Adw.Application):
    """ turtle application """
    window_class = None
    parameter = None

    def __init__(self, window_class=None, parameter=None):
        Adw.Application.__init__(self)
        self.set_flags(Gio.ApplicationFlags.NON_UNIQUE)
        self.set_application_id(turtlevcs.TURTLE_APP_ID)
        self.parameter = parameter

        if window_class:
            self.window_class = window_class
        self.connect('activate', self._on_activate)

    def _on_activate(self, app):
        try:
            if issubclass(self.window_class, DialogBase):
                if len(argv) > 1:
                    path = argv[1]
                else:
                    path = os.getcwd()
                if self.parameter:
                    window = self.window_class(path, self.parameter)
                else:
                    window = self.window_class(path)
            else:
                window = self.window_class()
        except Exception as ex:
            settings = turtlevcs.get_settings()
            full_trace = settings.get_boolean("full-exception-trace")

            error = f"{str(ex)}"

            window = Notification(error, title=f"Error in {self.window_class.__name__}")
            window.set_default_size(400, -1)

            if full_trace:
                expander = Gtk.Expander()
                overlay = Gtk.Overlay()
                button = Gtk.Button()
                button.set_icon_name("edit-copy-symbolic")
                button.set_halign(Gtk.Align.END)
                button.set_valign(Gtk.Align.END)
                overlay.add_overlay(button)
                label = Gtk.Label()
                trace = traceback.format_exc()
                label.set_label(trace)
                label.set_selectable(True)
                overlay.set_child(label)
                expander.set_label("Details")
                expander.set_child(overlay)
                window.set_extra_child(expander)

                def copy_trace(_button):
                    trace = label.get_label()
                    clipboard = Gdk.Display().get_default().get_clipboard()
                    clipboard.set(trace)

                button.connect("clicked", copy_trace)

            # raise exception for debug purposes
            # raise ex

        if isinstance(window, Gtk.Window):
            app.add_window(window)
            window.set_visible(True)
        elif isinstance(window.window, Gtk.Window):
            # special case for about window
            app.add_window(window.window)
            window.window.set_visible(True)
