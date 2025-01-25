""" settings dialog

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
from subprocess import check_output
import gi
import pygit2
import turtlevcs
from turtlevcs.dialogs import Notification, Information
from turtlevcs.turtle_app import TurtleApp
from turtlevcs.service import TurtleServiceConnector
from turtlevcs.dialogs.plugin_installer import PluginInstaller
from turtlevcs.dialogs.base import DialogBase

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw
from gi.repository import Gtk, Gio


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/settings.ui")
class SettingsWindow(Adw.PreferencesWindow, DialogBase):
    """ settings dialog """
    __gtype_name__ = "SettingsWindow"

    git_group = Gtk.Template.Child()
    git_name = Gtk.Template.Child()
    git_mail = Gtk.Template.Child()
    git_selected_credentials = Gtk.Template.Child()
    git_credential_ssh_agent = Gtk.Template.Child()
    git_credential_ssh_key = Gtk.Template.Child()
    git_agent = Gtk.Template.Child()
    git_ssh_key = Gtk.Template.Child()
    git_gpg_sign = Gtk.Template.Child()
    git_gpg_key = Gtk.Template.Child()
    git_https_password_row = Gtk.Template.Child()
    git_https_store_password = Gtk.Template.Child()
    plugins_enable_everywhere = Gtk.Template.Child()
    plugins_show_emblems = Gtk.Template.Child()
    plugins_show_turtle_emblem = Gtk.Template.Child()
    plugins_show_status_emblem_row = Gtk.Template.Child()
    plugins_show_status_emblem = Gtk.Template.Child()
    plugins_show_compare = Gtk.Template.Child()
    plugins_install_row = Gtk.Template.Child()
    dialogs_commit_selection = Gtk.Template.Child()
    dialogs_commit_unversioned = Gtk.Template.Child()
    dialogs_commit_ignored = Gtk.Template.Child()
    dialogs_stage_information = Gtk.Template.Child()
    git_store_password = Gtk.Template.Child()
    credentials_group = Gtk.Template.Child()
    debugging_full_trace = Gtk.Template.Child()
    service_page = Gtk.Template.Child()
    service_pid = Gtk.Template.Child()

    open_dialog = None

    repo = None
    settings = None

    def __init__(self, path=None):
        Adw.PreferencesWindow.__init__(self)
        DialogBase.__init__(self, path, no_turtle=True)

        self.settings = turtlevcs.get_settings()

        try:
            if path is not None:
                self.repo = pygit2.Repository(path)
        except Exception:
            pass

        try:
            if self.repo:
                author = turtlevcs.get_author(self.repo)
                self.git_name.set_text(author.name)
                self.git_mail.set_text(author.email)
            else:
                text = "only available inside repo"
                self.git_name.set_text(text)
                self.git_mail.set_text(text)
        except Exception as ex:
            window = Notification(str(ex), title="Could not get author information", parent=self)
            window.set_visible(True)

        if not turtlevcs.is_flatpak():
            self.plugins_install_row.set_visible(False)

        if not turtlevcs.can_store_password():
            self.git_https_password_row.set_visible(False)
            self.credentials_group.set_visible(False)

        self._init_settings()

        self._refresh_service_status()

    def _init_settings(self):
        if self.settings:
            # git
            self.settings.bind(
                "ssh-key",
                self.git_ssh_key,
                "text",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "agent",
                self.git_agent,
                "text",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "specific-ssh-key",
                self.git_credential_ssh_key,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "enable-store-passwords",
                self.git_https_store_password,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "gpg-auto-sign",
                self.git_gpg_sign,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "gpg-key",
                self.git_gpg_key,
                "text",
                Gio.SettingsBindFlags.DEFAULT)

            self.git_credential_ssh_key.set_active(self.settings.get_boolean("specific-ssh-key"))
            self._credential_type_changed_handler(self.git_credential_ssh_key)

            # plugins
            self.settings.bind(
                "enable-everywhere",
                self.plugins_enable_everywhere,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "show-emblems",
                self.plugins_show_emblems,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "show-turtle-emblem",
                self.plugins_show_turtle_emblem,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "show-status-emblem",
                self.plugins_show_status_emblem,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "show-compare",
                self.plugins_show_compare,
                "active",
                Gio.SettingsBindFlags.DEFAULT)

            # defaults
            # commit
            self.settings.bind(
                "commit-show-unversioned",
                self.dialogs_commit_unversioned,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "commit-show-ignored",
                self.dialogs_commit_ignored,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            self.settings.bind(
                "credentials-store-password",
                self.git_store_password,
                "active",
                Gio.SettingsBindFlags.DEFAULT)
            # cannot bind enum to AdwComboRow, sync it manually
            default_commit_selection = self.settings.get_enum("default-commit-selection")
            self.dialogs_commit_selection.set_selected(default_commit_selection)
            self.dialogs_commit_selection.connect(
                "notify::selected",
                self._on_dialogs_commit_selection_changed)
            # stage
            self.settings.bind(
                "stage-show-information",
                self.dialogs_stage_information,
                "active",
                Gio.SettingsBindFlags.DEFAULT)

            # debugging
            self.settings.bind(
                "full-exception-trace",
                self.debugging_full_trace,
                "active",
                Gio.SettingsBindFlags.DEFAULT)

    def _on_dialogs_commit_selection_changed(self, _widget, _property):
        default_commit_selection = self.dialogs_commit_selection.get_selected()
        self.settings.set_enum("default-commit-selection", default_commit_selection)


    @Gtk.Template.Callback()
    def _show_emblems_help_clicked(self, _widget):
        grid = Gtk.Grid()
        grid.set_row_spacing(6)
        grid.set_column_spacing(24)

        row = 0
        for s in pygit2.enums.FileStatus:
            icon = Gtk.Image.new_from_icon_name(turtlevcs.status_icon_map[s])
            grid.attach(icon, 0, row, 1, 1)

            label = Gtk.Label()
            label.set_label(turtlevcs.status_friendly_name_map[s])
            label.set_hexpand(True)
            label.set_halign(Gtk.Align.START)
            grid.attach(label, 1, row, 1, 1)

            row += 1

        information = Information(title="Emblems", content=grid, parent=self)
        information.set_visible(True)

    @Gtk.Template.Callback()
    def _install_files_plugin(self, _widget):
        installer = PluginInstaller(self)
        installer.present()

    @Gtk.Template.Callback()
    def _credential_type_changed_handler(self, _widget):
        is_agent = self.git_credential_ssh_agent.get_active()
        self.git_agent.set_sensitive(is_agent)
        self.git_ssh_key.set_sensitive(not is_agent)

    @Gtk.Template.Callback()
    def _search_ssh_key(self, _widget):
        if not self.open_dialog:
            self.open_dialog = Gtk.FileChooserNative.new(
                title="Choose an SSH private key",
                parent=self, action=Gtk.FileChooserAction.OPEN)
            self.open_dialog.connect("response", self._search_ssh_key_callback)
        path = self.git_ssh_key.get_text()
        if len(path) > 0 and os.path.exists(path):
            self.open_dialog.set_file(Gio.File.new_for_path(path))
        self.open_dialog.show()

    def _search_ssh_key_callback(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            path = dialog.get_file().get_path()
            if os.path.exists(path):
                self.git_ssh_key.set_text(path)

    @Gtk.Template.Callback()
    def _refresh_service_status(self, _widget=None):
        pids = []
        container = os.getenv("container")
        if not container:
            output = check_output(["ps", "x"]).decode("utf8")
            processes = output.split("\n")

            for process in processes:
                # check if the service runs in flatpak container
                if "/app/bin/turtle_service" in process:
                    values = process.strip().split(" ", 1)
                    pid = values[0]
                    pids.append(pid)

            if len(pids) > 0:
                container = "flatpak, real pid: " + ",".join(pids)

        try:
            turtle_service = TurtleServiceConnector()
            current_pid = turtle_service.get_pid()

            self.service_pid.set_label(
                str(current_pid) + (" (" + container + ")" if container else ""))
        except Exception as _ex:
            self.service_pid.set_label("(unavailable)")


if __name__ == "__main__":
    TurtleApp(SettingsWindow).run()
