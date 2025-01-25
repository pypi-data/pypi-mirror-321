""" nautilus plugin installer

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
from pathlib import Path
import gi
from turtlevcs.turtle_app import TurtleApp

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gdk


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/plugin_installer.ui")
class PluginInstaller(Adw.MessageDialog):
    """ add dialog """
    __gtype_name__ = "PluginInstaller"

    label_path = Gtk.Template.Child()

    def __init__(self, parent=None):
        Adw.MessageDialog.__init__(self, transient_for=parent)

        self.src_path = Path("/app/share/nautilus-python/extensions")
        self.dst_path = Path(Path.home()) / ".local/share/nautilus-python/extensions"
        self.plugin_file = "turtle_nautilus_flatpak.py"

        css_provider = Gtk.CssProvider()
        css_provider.load_from_string(""".code {
  padding-left: 8px;
  padding-right: 8px;
  border-radius: 8px;
}
""")
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.label_path.add_css_class("view")
        self.label_path.add_css_class("frame")
        self.label_path.add_css_class("code")
        self.label_path.add_css_class("dim-label")
        self.label_path.set_label(f"{self.dst_path}")

        self.add_response("ok", "Install")
        self.add_response("cancel", "Cancel")

        self.connect("response", self._on_response)

    def _on_response(self, _dialog, response):
        if response == "ok":
            os.makedirs(self.dst_path, exist_ok=True)
            shutil.copy(self.src_path / self.plugin_file, self.dst_path / self.plugin_file)

    @Gtk.Template.Callback()
    def _copy_path_clicked(self, _button):
        clipboard = Gdk.Display().get_default().get_clipboard()
        path = self.label_path.get_label()
        clipboard.set(path)


if __name__ == "__main__":
    TurtleApp(PluginInstaller).run()
