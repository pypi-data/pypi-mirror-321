""" dialogs module

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
import sys
import threading
import subprocess
import gi
import turtlevcs
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk, GLib


class Notification(Adw.MessageDialog):
    """ notification dialog, shows a message and has an ok button """

    def __init__(self, message, title=None, parent=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        if title:
            self.set_heading(title)
        self.set_body(message)

        self.add_response("ok", "Ok")

class Information(Adw.MessageDialog):
    """ information dialog, shows content and has a close button """

    def __init__(self, title=None, content=None, parent=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        if title:
            self.set_heading(title)
        if isinstance(content, type(str)):
            self.set_body(content)
        elif content:
            self.set_extra_child(content)

        self.add_response("ok", "Close")


class Progress(Adw.MessageDialog, threading.Thread):
    """ progress dialog, runs a function in a thread and shows its progress """
    functions = None
    running = False
    box = None
    progress_bar = None
    close_on_finish = False

    def __init__(self, message, functions, parent=None, start_automatically=True):
        Adw.MessageDialog.__init__(self, transient_for=parent)
        threading.Thread.__init__(self, target=self._thread_function)

        self.set_heading(message)
        self.box = Gtk.Box()
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.pulse()
        self.box.append(self.progress_bar)
        self.set_extra_child(self.box)
        self.add_response("yes", "Ok")
        self.set_response_enabled("yes", False)

        if isinstance(functions, list):
            self.functions = functions
        else:
            self.functions = [functions]

        if start_automatically:
            self.connect("show", self._start_on_show)

    def _start_on_show(self, _widget):
        # start the thread once the progress window is shown
        # so DialogBase._set_progress_message works properly
        self.start()

    def run(self):
        threading.Thread.run(self)

        self.set_response_enabled("yes", True)

    def _thread_function(self):
        self.running = True
        GLib.timeout_add(100, self._pulse)

        for function in self.functions:
            if function and callable(function):
                try:
                    function()
                except Exception as ex:
                    self.set_body(f"error: {str(ex)}")
                    self.close_on_finish = False

        self.running = False

    def _pulse(self):
        if self.running:
            self.progress_bar.pulse()
        else:
            self.progress_bar.set_fraction(1.0)
            if self.close_on_finish:
                self.close()

        return self.running


class Question(Adw.MessageDialog):
    """ question dialog, shows a question and has yes, no buttons """
    callback = None
    data = None

    def __init__(self, title, callback, data=None, message=None, parent=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)
        self.callback = callback
        self.data = data

        self.set_heading(title)
        if message:
            self.set_body(message)
        self.add_response("yes", "Yes")
        self.add_response("no", "No")
        self.connect("response", self._on_response)

    def _on_response(self, _widget, response):
        confirm = response == "yes"
        if self.callback:
            if self.data:
                self.callback(confirm, self.data)
            else:
                self.callback(confirm)

class MultilineInput(Adw.MessageDialog):
    """ input dialog to enter multiline texts and has ok, cancel buttons """
    callback = None

    def __init__(self, message, callback, parent=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)
        self.callback = callback

        self.set_heading("Message")
        self.set_body("Enter a multiline commit message here.")
        scrolled = Gtk.ScrolledWindow()
        text_view = Gtk.TextView()
        text_view.get_buffer().set_text(message)
        scrolled.set_child(text_view)
        scrolled.set_size_request(300, 100)
        self.set_extra_child(scrolled)
        self.add_response("ok", "Ok")
        self.add_response("cancel", "Cancel")
        self.connect("response", self._on_response)

    def _on_response(self, widget, response):
        confirm = response == "ok"
        if self.callback:
            buffer = widget.get_extra_child().get_child().get_buffer()
            start, end = buffer.get_bounds()
            new_message = buffer.get_text(start, end, False)
            self.callback(confirm, new_message)

class Subprocess(Progress):
    """ subprocess dialog, shows a message while waiting for a subprocess to close """

    process_args = []
    # temp file objects needed for meld
    temp_file1 = None
    temp_file2 = None

    def __init__(self, process_args, parent=None, start_automatically=True):
        Progress.__init__(self, "", None, parent=parent, start_automatically=False)

        self.process_args = process_args

        self.set_heading("Waiting")
        self.set_body("Subprocess still running, waiting for it to close.")

        self.functions = [self._run_subprocess]
        self.close_on_finish = True

        if start_automatically:
            self.start()

    def _run_subprocess(self):
        self.set_body(
            f"Subprocess '{self.process_args[0]}' still running, waiting for it to close.")
        subprocess.run(self.process_args, check=False)

        if self.temp_file1 is not None:
            self.temp_file1.close()
        if self.temp_file2 is not None:
            self.temp_file2.close()

class QuickSettings(Adw.MessageDialog):
    """ quick settings dialog, used for local repository settings """

    def __init__(self, title, message=None, settings=None, parent=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        self.set_heading(title)
        if message is not None:
            self.set_body(message)

        if settings is not None:
            self.set_extra_child(settings)

        self.add_response("ok", "Ok")


def _on_activate(app):
    args = sys.argv

    if len(args) > 1:
        notification = Notification(args[1])
        app.add_window(notification)
        notification.set_visible(True)

if __name__ == "__main__":
    APP = Adw.Application()
    APP.set_application_id(turtlevcs.TURTLE_APP_ID)
    APP.connect('activate', _on_activate)
    APP.run()
