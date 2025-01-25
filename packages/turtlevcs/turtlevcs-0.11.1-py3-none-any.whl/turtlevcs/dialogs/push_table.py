""" push table

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
from datetime import datetime, timezone
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject


class PushListModelEntry(GObject.Object):
    """ an entry in the push model, which represents a single commit """
    date = None
    short_id = None
    message = None

    def __init__(self, date, short_id, message):
        GObject.Object.__init__(self)

        if date is not None:
            timestamp = datetime.fromtimestamp(date, timezone.utc).astimezone()
            time_diff = datetime.now(timezone.utc).astimezone() - timestamp

            if time_diff.days < 1:
                self.date = timestamp.strftime("%H:%M")
            elif time_diff.days < 7:
                self.date = timestamp.strftime("%a, %H:%M")
            else:
                self.date = timestamp.strftime("%Y-%m-%d")
        else:
            self.date = ""

        self.short_id = short_id if short_id is not None else ""
        # strip potential newlines from message
        self.message = message.strip()
        self.message = self.message.split("\n")[0]


class PushListModel(Gio.ListStore):
    """ push model contains commits to push """

    def __init__(self):
        Gio.ListStore.__init__(self)


@Gtk.Template(filename=f"{os.path.dirname(os.path.abspath(__file__))}/ui/push_table.ui")
class PushTable(Gtk.ColumnView):
    """ push table """
    __gtype_name__ = "PushTable"

    selection_model = Gtk.Template.Child()
    column_date = Gtk.Template.Child()
    column_hash = Gtk.Template.Child()

    model = None
    is_updating = False

    branch_name = None
    remote_name = None

    def __init__(self, turtle):
        Gtk.ColumnView.__init__(self)

        self.turtle = turtle

    def update_commits(self, branch_name, remote_name):
        """ update commit table, returns True if a push is possible """

        self.model = PushListModel()
        self.selection_model.set_model(self.model)

        commit_list, branch_on_remote = self.turtle.get_commits_for_push(
            branch_name=branch_name, remote_name=remote_name)

        for commit in commit_list:
            self.model.append(PushListModelEntry(
                date=commit.commit_time, short_id=commit.short_id, message=commit.message))

        if self.model.get_n_items() < 1 and not branch_on_remote:
            self.column_date.set_visible(False)
            self.column_hash.set_visible(False)
            self.model.append(PushListModelEntry(
                date=None,
                short_id=None,
                message="all commits are on remote already, but branch is not available yet"))
        else:
            self.column_date.set_visible(True)
            self.column_hash.set_visible(True)

        return branch_name and remote_name

    @Gtk.Template.Callback()
    def _column_date_setup_handler(self, _factory, listitem):
        label = Gtk.Label()
        listitem.set_child(label)

    @Gtk.Template.Callback()
    def _column_date_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        label = listitem.get_child()
        label.set_label(item.date)

    @Gtk.Template.Callback()
    def _column_hash_setup_handler(self, _factory, listitem):
        label = Gtk.Label()
        listitem.set_child(label)

    @Gtk.Template.Callback()
    def _column_hash_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        label = listitem.get_child()
        label.set_label(item.short_id)

    @Gtk.Template.Callback()
    def _column_message_setup_handler(self, _factory, listitem):
        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        listitem.set_child(label)

    @Gtk.Template.Callback()
    def _column_message_bind_handler(self, _factory, listitem):
        item = listitem.get_item()
        label = listitem.get_child()
        label.set_label(item.message)
        label.set_sensitive(len(item.date) > 0)

    @Gtk.Template.Callback()
    def _column_teardown_handler(self, _factory, listitem):
        listitem.set_child(None)

    @Gtk.Template.Callback()
    def _column_unbind_handler(self, _factory, listitem):
        label = listitem.get_child()
        label.set_label("")
