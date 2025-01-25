""" turtlevcs module

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
import sys
import subprocess
import argparse
import textwrap
from threading import Condition
from gi.repository import Gio
from turtlevcs.package_information import VERSION

TURTLE_APP_ID = "de.philippun1.turtle"

try:
    import pygit2

    status_icon_map = {
        pygit2.enums.FileStatus.CURRENT: "emblem-default",
        pygit2.enums.FileStatus.INDEX_NEW: "emblem-new",
        pygit2.enums.FileStatus.INDEX_MODIFIED: "emblem-important",
        pygit2.enums.FileStatus.INDEX_DELETED: "edit-delete",
        pygit2.enums.FileStatus.INDEX_RENAMED: "emblem-symbolic-link",
        pygit2.enums.FileStatus.INDEX_TYPECHANGE: "dialog-question",
        pygit2.enums.FileStatus.WT_NEW: "dialog-question",
        pygit2.enums.FileStatus.WT_MODIFIED: "emblem-important",
        pygit2.enums.FileStatus.WT_DELETED: "edit-delete",
        pygit2.enums.FileStatus.WT_TYPECHANGE: "dialog-question",
        pygit2.enums.FileStatus.WT_RENAMED: "emblem-symbolic-link",
        pygit2.enums.FileStatus.WT_UNREADABLE: "emblem-readonly",
        pygit2.enums.FileStatus.IGNORED: "emblem-dropbox-selsync",
        pygit2.enums.FileStatus.CONFLICTED: "software-update-urgent",
    }

    status_friendly_name_map = {
        pygit2.enums.FileStatus.CURRENT: "normal",
        pygit2.enums.FileStatus.INDEX_NEW: "new (staged)",
        pygit2.enums.FileStatus.INDEX_MODIFIED: "modified (staged)",
        pygit2.enums.FileStatus.INDEX_DELETED: "deleted (staged)",
        pygit2.enums.FileStatus.INDEX_RENAMED: "renamed (staged)",
        pygit2.enums.FileStatus.INDEX_TYPECHANGE: "type changed (staged)",
        pygit2.enums.FileStatus.WT_NEW: "new",
        pygit2.enums.FileStatus.WT_MODIFIED: "modified",
        pygit2.enums.FileStatus.WT_DELETED: "deleted",
        pygit2.enums.FileStatus.WT_TYPECHANGE: "type changed",
        pygit2.enums.FileStatus.WT_RENAMED: "renamed",
        pygit2.enums.FileStatus.WT_UNREADABLE: "unreadable",
        pygit2.enums.FileStatus.IGNORED: "ignored",
        pygit2.enums.FileStatus.CONFLICTED: "conflicted",
    }

    delta_status_icon_map = {
        pygit2.enums.DeltaStatus.ADDED: "emblem-new",
        pygit2.enums.DeltaStatus.CONFLICTED: "software-update-urgent",
        pygit2.enums.DeltaStatus.COPIED: "emblem-symbolic-link",
        pygit2.enums.DeltaStatus.DELETED: "edit-delete",
        pygit2.enums.DeltaStatus.IGNORED: "emblem-dropbox-selsync",
        pygit2.enums.DeltaStatus.MODIFIED: "emblem-important",
        pygit2.enums.DeltaStatus.RENAMED: "emblem-symbolic-link",
        pygit2.enums.DeltaStatus.TYPECHANGE: "dialog-question",
        pygit2.enums.DeltaStatus.UNMODIFIED: "emblem-default",
        pygit2.enums.DeltaStatus.UNREADABLE: "emblem-readonly",
        pygit2.enums.DeltaStatus.UNTRACKED: "dialog-question",
    }

    STATUS_WT_BITMAP = (
        pygit2.enums.FileStatus.CONFLICTED +
        pygit2.enums.FileStatus.WT_DELETED +
        pygit2.enums.FileStatus.WT_MODIFIED +
        pygit2.enums.FileStatus.WT_NEW +
        pygit2.enums.FileStatus.WT_RENAMED +
        pygit2.enums.FileStatus.WT_TYPECHANGE +
        pygit2.enums.FileStatus.WT_UNREADABLE)

    STATUS_INDEX_BITMAP = (
        pygit2.enums.FileStatus.INDEX_DELETED +
        pygit2.enums.FileStatus.INDEX_MODIFIED +
        pygit2.enums.FileStatus.INDEX_NEW +
        pygit2.enums.FileStatus.INDEX_RENAMED +
        pygit2.enums.FileStatus.INDEX_TYPECHANGE)
except Exception as _ex:
    pass

def has_index_status(status):
    """ check if a status contains an index status """
    index_status = status & STATUS_INDEX_BITMAP
    return index_status > 0, index_status

def has_worktree_status(status):
    """ check if a status contains an index status """
    wt_status = status & STATUS_WT_BITMAP
    return wt_status > 0, wt_status

def get_full_version():
    """ get full version string of turtle """
    try:
        repo = pygit2.Repository(os.path.realpath(__file__))
        return f"{VERSION}-{repo.get(str(repo.head.target)).short_id}"
    except Exception:
        pass
    return VERSION

def launch_dialog(module, args):
    """ helper function to launch a turtle dialog """
    basedir, _ = os.path.split(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(basedir, "turtlevcs", "dialogs", module + ".py")

    executable = sys.executable
    if os.path.exists(path):
        if "PYTHON" in list(os.environ):
            executable = os.environ["PYTHON"]
        subprocess.run([executable, path] + args, cwd=os.getcwd(), check=False)

    else:
        path = os.path.join(basedir, "turtlevcs", "dialogs", "__init__.py")
        if os.path.exists(path):
            subprocess.run([executable, path, "turtlevcs module '" +
                           module + "' not available"], cwd=basedir, check=False)


def get_author(repo):
    """ get the author signature """
    if isinstance(repo, pygit2.Repository):
        return repo.default_signature
    return None


def get_keypair():
    """ get the ssh keypair """
    settings = get_settings()
    if settings:
        if settings.get_boolean("specific-ssh-key"):
            key = settings.get_string("ssh-key")
            if len(key) > 0 and os.path.exists(key):
                return pygit2.Keypair(None, f"{key}.pub", key, None)
        else:
            agent = settings.get_string("agent")
            if len(agent) > 0:
                return pygit2.KeypairFromAgent(agent)

    raise UserWarning("no credentials available")

def can_store_password():
    """
    password can only be stored if secretstorage is available
    and the application is not running in a flatpak
    """
    has_storage = False
    try:
        import secretstorage
        has_storage = True
    except ImportError:
        pass

    return has_storage and not is_flatpak()

def get_credentials_from_dialog(url, username_from_url):
    """ open a dialog to get credentials """
    condition = Condition()

    from turtlevcs.dialogs.enter_credentials import EnterCredentials

    credentials = EnterCredentials(
        parent=None,
        url=url,
        username_from_url=username_from_url,
        condition=condition)

    with condition:
        condition.wait()

    return credentials.get_credentials()

def get_settings():
    """ get the gio settings object """
    source = Gio.SettingsSchemaSource.get_default()
    schema = source.lookup(TURTLE_APP_ID, True)
    if schema is not None:
        settings = Gio.Settings(schema_id=TURTLE_APP_ID)
        return settings

    return None

def is_flatpak():
    """ check if the application is running in a flatpak """
    return os.getenv("container") is not None

def create_parser(program, description):
    """ create a parser for the command line """
    modules = {
        "about": "Display information about Turtle",
        "add": "Add file(s) to the index",
        "checkout": "Checkout a branch or commit",
        "clone": "Clone a repository into a new directory",
        "commit": "Commit changes to the repository",
        "clean": "Clean untracked files in a repository",
        "create_branch": "Create a branch",
        "create_tag": "Create a tag",
        "diff_file": "Show current changes of a file",
        "diff": "Show changes between commits",
        "init": "Create an empty repository",
        "log": "Show commit logs",
        "merge": "Merge a branch or commit into current HEAD",
        "plugin_installer": "Install the nautilus plugin from the flatpak",
        "pull": "Pull the current branch",
        "push": "Push a branch",
        "references": "Show references",
        "remotes": "Manage remotes",
        "reset": "Reset current branch to a specific reference",
        "resolve": "Resolve conflicts in the working tree",
        "revert": "Revert changed files in the working tree",
        "settings": "Show and modify settings",
        "stage": "Stage a file",
        "submodules": "Initialize, update or inspect submodules",
        "sync": "Pull, push or fetch changes from or to a remote repository",
        "unstage": "Unstage a file",
        "update": "Update a branch",
    }
    parser = argparse.ArgumentParser(
        prog=program,
        description=textwrap.indent(
            textwrap.dedent(
                f"""
                Turtle {description}
                """
            ).strip(),
            "    "
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "module",
        choices=modules.keys(),
        help="\n".join([f"{k}:\t{v}".expandtabs(16) for k, v in modules.items()]).strip(),
    )

    parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help="arguments for the module (path, etc.)"
    )

    return parser
