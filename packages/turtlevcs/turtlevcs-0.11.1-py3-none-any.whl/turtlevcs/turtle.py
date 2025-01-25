""" turtle

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
import re
import tempfile
import pathlib
import shutil
from enum import Enum
import pygit2
import pygit2.enums
import turtlevcs

class PullAction(Enum):
    """ enum type for pull actions """
    FETCH_ONLY = 0
    FETCH_AND_MERGE = 1
    FETCH_AND_REBASE = 2

class CreateFrom(Enum):
    """ enum type from which, i.e. a branch will be created from """
    HEAD = 0
    BRANCH = 1
    COMMIT = 2
    WORKING_COPY = 3

class TurtleCallbacks(pygit2.RemoteCallbacks):
    """ callback class for remote actions """

    agent = False
    user_pass = None
    storage_searched = None
    url = None
    store_password = False
    progress_callback = None

    def __init__(self, progress_callback=None):
        pygit2.RemoteCallbacks.__init__(self)

        self.progress_callback = progress_callback

    def credentials(self, url, username_from_url, allowed_types):
        if pygit2.enums.CredentialType.USERPASS_PLAINTEXT in allowed_types:
            settings = turtlevcs.get_settings()
            storage_enabled = settings.get_boolean("enable-store-passwords")
            if self.storage_searched is False and storage_enabled:
                # we only try to search the credentials once
                self.storage_searched = True
                if turtlevcs.can_store_password():
                    self.user_pass = self._search_credentials_for_url(url, username_from_url)
                    if self.user_pass is not None:
                        return self.user_pass

            user, password, self.store_password = turtlevcs.get_credentials_from_dialog(
                url, username_from_url)

            self.user_pass = pygit2.credentials.UserPass(user, password)
            self.url = url

            return self.user_pass
        elif pygit2.enums.CredentialType.SSH_KEY in allowed_types:
            return turtlevcs.get_keypair()
        else:
            raise RuntimeError("Unsupported credential type")

    def push_update_reference(self, _refname, message):
        if message is not None:
            raise RuntimeError(f"push failed: {message}")

    def transfer_progress(self, stats):
        """ transfer_progress """
        if self.progress_callback and callable(self.progress_callback):
            self.progress_callback(
                f"{stats.indexed_objects} / {stats.total_objects} objects")

    def save(self):
        """ save used credentials """
        if self.store_password and self.user_pass is not None:
            settings = turtlevcs.get_settings()
            storage_enabled = settings.get_boolean("enable-store-passwords")
            if not turtlevcs.can_store_password() or not storage_enabled:
                return

            try:
                import secretstorage
                conn = secretstorage.dbus_init()
                collection = secretstorage.get_default_collection(conn)

                user, password = self.user_pass.credential_tuple

                _item = collection.create_item(label=f"Turtle UserPass {self.url}", attributes={
                    "application": turtlevcs.TURTLE_APP_ID,
                    "url": self.url,
                    "user": user,
                    }, secret=password)
            except ImportError:
                pass

    def _search_credentials_for_url(self, url, user):
        try:
            import secretstorage
            conn = secretstorage.dbus_init()
            collection = secretstorage.get_default_collection(conn)

            search_map = {
                "application": turtlevcs.TURTLE_APP_ID,
                "url": url
            }
            if user is not None:
                search_map["user"] = user

            items = collection.search_items(search_map)

            for item in items:
                # we take the first available item matching the search criteria
                user, password = item.get_attributes()["user"], item.get_secret().decode()
                return pygit2.UserPass(user, password)
        except ImportError:
            pass


class TurtleBase():
    """ a base class which creates and contains a turtle object """
    path = None
    turtle = None

    def __init__(self, path, no_turtle=False):
        self.path = path
        if no_turtle is False:
            self.turtle = Turtle(path)

class Turtle():
    """ turtle who takes care of the git stuff """
    repo = None

    def __init__(self, path):
        self.repo = pygit2.Repository(path)

    def reload(self):
        """ reload pygit2 repository """
        self.repo = pygit2.Repository(self.repo.workdir)

    def get_repo_name(self):
        """ get the repository name (basically the local folder name) """
        # TODO is this the best way to find the "repository name"?
        try:
            name = self.repo.path
            name = name.removesuffix("/.git/")
            pieces = name.split("/")
            name = pieces[-1]
        except Exception:
            name = ""

        return name

    def get_current_commit_hex(self):
        """ get hex of the currently checked out commit """
        return str(self.repo.head.target)

    def get_current_branch_name(self):
        """ get name of the currently checked out branch """
        try:
            branch_name = self.repo.head.shorthand
        except Exception:
            # we do not have a branch name if there is no commit yet in a fresh repo
            branch_name = "-"
        return branch_name

    def get_commit_info(self, show_unversioned, show_ignored, amend=False):
        """ get relevant commit info """
        message = None

        untracked_files = "all"
        if not show_unversioned:
            untracked_files = "no"

        if amend:
            branch = self.repo[self.repo.head.target]
            message = branch.message

        status = self.repo.status(
            untracked_files=untracked_files, ignored=show_ignored)

        return status, message

    def add(self, files, deleted_files):
        """ add files """

        index = self.repo.index
        total = len(files)
        for file in files:
            index.add(file)

        total_deleted = len(deleted_files)
        for file in deleted_files:
            index.remove(file)

        if total > 0 or total_deleted > 0:
            index.write()

        return total + total_deleted

    def commit(self, message, amend, files, deleted_files, gpg_sign=False, gpg_key=None):
        """ commit files """
        error = None
        is_merge = False
        merge_head = None
        total = 0

        if amend and gpg_sign:
            error = "Cannot amend and sign at the same time"
            return total, error

        try:
            ref = self.repo.head.name
            parents = [self.repo.head.target]
            is_merge, merge_head = self.is_merge_in_progress()
            if is_merge:
                parents.append(merge_head)
        except Exception:
            ref = "HEAD"
            parents = []
            amend = False

        index = self.repo.index

        for file in files:
            index.add(file)

        for file in deleted_files:
            index.remove(file)

        if self.repo.head_is_unborn:
            total = -1
        else:
            diff = self.repo.diff("HEAD", cached=True)
            total = diff.stats.files_changed

        if total > 0 or amend or self.repo.head_is_unborn:
            index.write()

            try:
                tree = index.write_tree()

                signature = turtlevcs.get_author(self.repo)

                if amend:
                    commit = self.repo[self.repo.head.target]
                    self.repo.amend_commit(
                        commit, "HEAD", None, signature, message, tree)
                elif gpg_sign:
                    commit_string = self.repo.create_commit_string(
                        signature, signature, message, tree, parents)
                    signed_string = sign_message(commit_string, gpg_key)
                    commit = self.repo.create_commit_with_signature(commit_string, signed_string)
                    self.repo.head.set_target(commit)
                else:
                    self.repo.create_commit(
                        ref, signature, signature, message, tree, parents)

                if is_merge:
                    self.repo.state_cleanup()
            except Exception as ex:
                total = 0
                error = str(ex)

        return total, error

    def get_push_info(self):
        """ get relevant push info """
        try:
            current_branch_name = self.repo.head.shorthand
        except Exception:
            current_branch_name = None

        try:
            current_branch = self.repo.branches.local[current_branch_name]
        except Exception:
            current_branch = None

        try:
            current_remote = current_branch.upstream.remote_name
        except Exception:
            current_remote = None

        return current_remote, current_branch_name, self.repo.branches.local, self.repo.remotes

    def get_commits_for_push(self, branch_name, remote_name):
        """ get commits to be pushed """

        commit_list = []
        branch_on_remote = False

        try:
            branch = self.repo.branches.get(branch_name)

            latest_commit_id = str(branch.target)
            latest_commit = self.repo.revparse_single(latest_commit_id)

            if remote_name is not None:
                try:
                    remote_branch = self.repo.branches.remote[remote_name + "/" + branch_name]
                    if remote_branch is not None:
                        branch_on_remote = True
                except Exception as _ex:
                    pass

                commit_list = self.repo.walk(
                    latest_commit.id, pygit2.enums.SortMode.TIME)

                # hide all commits existing on target remote from list
                for remote_branch_name in self.repo.branches.remote:
                    remote_branch = self.repo.branches[remote_branch_name]
                    if remote_branch.remote_name == remote_name:
                        first_commit = self.repo.revparse_single(remote_branch.name)
                        commit_list.hide(first_commit.id)
        except Exception as _ex:
            pass

        return commit_list, branch_on_remote

    def push(self, branch_name, remote_name):
        """ push branch to remote """
        if branch_name is None or len(branch_name) == 0:
            branch_name = self.repo.head.shorthand
        branch = self.repo.branches[branch_name]
        if remote_name is None or len(remote_name) == 0:
            if branch.upstream:
                remote_name = branch.upstream.remote_name
            else:
                remote_name = self.repo.remotes[0].name
        remote = self.repo.remotes[remote_name]

        refspec = branch.name
        callbacks = TurtleCallbacks()
        remote.push([refspec], callbacks)

        if branch.upstream is None:
            branch.upstream = self.repo.branches[f"{remote_name}/{branch_name}"]

        callbacks.save()

    def get_branch_upstream(self, branch_name):
        """ get the upstream branch to local branch, i.e. to check if it can be pulled """
        branch = self.repo.branches[branch_name]
        return branch.upstream

    def pull(self, branch_name, remote_name, pull_action):
        """ pull a branch from remote """
        title = None
        message = None
        if self.repo.head_is_detached or self.repo.head_is_unborn:
            if pull_action is PullAction.FETCH_ONLY and len(self.repo.remotes) == 1:
                remote_name = self.repo.remotes[0].name
            else:
                raise RuntimeError("HEAD is detached")

        else:
            if not branch_name:
                branch_name = self.repo.head.shorthand

            if not remote_name:
                branch = self.repo.branches[branch_name]
                remote_name = branch.upstream.remote_name

        remote = self.repo.remotes[remote_name]
        callbacks = TurtleCallbacks()
        remote.fetch(callbacks=callbacks)

        callbacks.save()

        if pull_action is not PullAction.FETCH_ONLY:
            branch = self.repo.branches[branch_name]
            merge_result, _ = self.repo.merge_analysis(branch.upstream.target)
            if merge_result & pygit2.enums.MergeAnalysis.UP_TO_DATE:
                pass # do nothing

            elif merge_result & pygit2.enums.MergeAnalysis.FASTFORWARD:
                self.repo.checkout_tree(self.repo.get(branch.upstream.target))
                branch.set_target(branch.upstream.target)
                self.repo.head.set_target(branch.upstream.target)

            elif merge_result & pygit2.enums.MergeAnalysis.NORMAL:
                if pull_action is PullAction.FETCH_AND_REBASE:
                    pass # TODO rebase
                else:
                    self.repo.merge(branch.upstream.target)

                    if self.repo.index.conflicts is None:
                        self._do_merge_commit(
                            self.repo.index,
                            branch.upstream.target,
                            branch.upstream.shorthand)
                    else:
                        title = "Conflicts"
                        message = "Fix conflicts and then commit the result"

            else:
                message = "Merge failed"

        return message, title

    def log(self, all_branches=False, ignored_remotes=[], hide_local=False):
        """ get commit log of current branch """
        commit_list = []

        if all_branches:
            head_id = self.repo.head.target
            seen = []

            walker = self.repo.walk(None, pygit2.enums.SortMode.TOPOLOGICAL)

            def add_target_to_list(branch, skip_head=True):
                nonlocal commit_list
                try:
                    target_id = branch.resolve().target
                except Exception as _ex:
                    target_id = head_id

                if skip_head and not hide_local and target_id == head_id:
                    return

                walker.push(target_id)
                for s in seen:
                    walker.hide(s)
                seen.append(target_id)
                commit_list_temp = []

                for commit in walker:
                    commit_list_temp.append(commit)

                if len(commit_list_temp) > 0:
                    commit_list = commit_list_temp + commit_list


            # add local branches
            if not hide_local:
                for branch_name in self.repo.branches.local:
                    branch = self.repo.branches[branch_name]
                    add_target_to_list(branch)

            # add remote branches
            for branch_name in self.repo.branches.remote:
                branch = self.repo.branches[branch_name]

                if branch.remote_name in ignored_remotes:
                    continue

                add_target_to_list(branch)

            if not hide_local:
                # try to add the head last, so it appears on top
                # will not be possible if head is part of a branch
                add_target_to_list(head_id, skip_head=False)

        else:
            latest_commit_id = str(self.repo.head.target)
            latest_commit = self.repo.revparse_single(latest_commit_id)
            walker = self.repo.walk(latest_commit.id, pygit2.enums.SortMode.TOPOLOGICAL)
            for commit in walker:
                commit_list.append(commit)

        return commit_list

    def get_full_file_path(self, file):
        """ get the full file path for a file in the repo """
        return pathlib.Path(self.repo.workdir) / file

    def get_relative_file_path(self, file):
        """ get the full file path for a file in the repo """
        return file.removeprefix(self.repo.workdir)

    def get_file_from_index(self, file):
        """ store content of file from index into a tmp file and return temp file object """
        file_path = file.split("/")[-1]
        temp = tempfile.NamedTemporaryFile(suffix=f"__INDEX_{file_path}")

        index = self.repo.index
        index.read()
        try:
            identifier = index[file].id
            blob = self.repo[identifier]

            temp.write(blob.data)
            temp.flush()
        except Exception as _ex:
            temp.close()

        return temp

    def get_file_from_commit(self, commit_hex, file):
        """ store content of file from a commit into a tmp file and return temp file object """

        temp = None
        try:
            index = pygit2.Index()
            commit = self.repo.revparse_single(commit_hex)

            file_path = file.split("/")[-1]
            temp = tempfile.NamedTemporaryFile(suffix=f"__{commit.short_id}_{file_path}")

            index.read_tree(commit.tree)
            identifier = index[file].id
            blob = self.repo[identifier]

            temp.write(blob.data)
            temp.flush()
        except Exception as _ex:
            if temp:
                temp.close()

        return temp

    def get_file_from_previous_commit(self, file):
        """ store content of file from previous commit into a tmp file and return file object """
        prev_commit = self.repo.revparse_single(self.repo.head.name)
        commit_hex = str(prev_commit.id)

        return self.get_file_from_commit(commit_hex, file)

    def get_branch_commit_dictionary(self, ignored_remotes=[], hide_local=False):
        """ get a dictionary [commit] = branch """
        branch_dict = {}

        def add_branch_to_dict(branch):
            if not isinstance(branch.target, str):
                if str(branch.target) in branch_dict:
                    branch_dict[str(branch.target)].append((branch.name, branch_name))
                else:
                    branch_dict[str(branch.target)] = [(branch.name, branch_name)]

        if not hide_local:
            for branch_name in self.repo.branches.local:
                add_branch_to_dict(self.repo.branches[branch_name])

        for branch_name in self.repo.branches.remote:
            branch = self.repo.branches[branch_name]
            if branch.remote_name not in ignored_remotes:
                add_branch_to_dict(branch)

        return branch_dict

    def get_tag_commit_dictionary(self, tag_dict={}):
        """ get a dictionary [commit] = tag """

        regex = re.compile('^refs/tags/')
        for ref_name in self.repo.references:
            if regex.match(ref_name):
                ref = self.repo.references[ref_name]
                commit = str(ref.target)
                if commit in tag_dict:
                    tag_dict[commit].append((ref.name, ref.shorthand))
                else:
                    tag_dict[commit] = [(ref.name, ref.shorthand)]

        return tag_dict

    def get_list_of_references(self):
        """ get list of all available references """
        ref_list = []

        for ref in self.repo.references:
            ref_list.append(ref)

        return ref_list

    def get_list_of_branches(self):
        """ get list of all available branches """
        branch_list = []
        for branch_name in self.repo.branches:
            branch = self.repo.branches[branch_name]
            if not isinstance(branch.target, str):
                branch_list.append(branch_name)

        return branch_list

    def checkout(
            self,
            name,
            new_branch_name=None,
            force=False,
            override=False):
        """ checkout a branch, tag or commit """

        strategy = \
            pygit2.enums.CheckoutStrategy.FORCE if force else pygit2.enums.CheckoutStrategy.SAFE
        is_remote_branch = False

        if name.startswith("refs/"):
            branch_name = name.split("/", 2)[-1]
        else:
            branch_name = name
        is_branch = self.repo.lookup_branch(branch_name, pygit2.enums.BranchType.ALL)
        is_remote_branch = self.repo.lookup_branch(branch_name, pygit2.enums.BranchType.REMOTE)

        if is_branch:
            branch = self.repo.branches[branch_name]

            if is_remote_branch:
                new_branch_name = branch.shorthand.removeprefix(
                    branch.remote_name).removeprefix("/")

            ref = self.repo.lookup_reference(branch.name)
            self.repo.checkout(refname=ref, strategy=strategy)
        else:
            # tag or commit hash
            commit = self.repo.revparse_single(name)
            self.repo.checkout_tree(treeish=commit, strategy=strategy)
            self.repo.set_head(commit.id)

        if new_branch_name:
            commit = self.repo.revparse_single(self.repo.head.name)
            new_branch = self.repo.branches.create(new_branch_name, commit, override)
            if is_remote_branch:
                new_branch.upstream = self.repo.branches[branch_name]

            new_ref = self.repo.lookup_reference(new_branch.name)
            self.repo.checkout(refname=new_ref, strategy=strategy)

    def init_submodules(self, external_callbacks=None, repo=None):
        """ init all submodules recursively """
        # TODO not tested yet
        if repo is None:
            repo=self.repo

        callbacks = external_callbacks if external_callbacks else TurtleCallbacks()

        submodules = repo.listall_submodules()
        repo.submodules.init(submodules=submodules)
        repo.submodules.update(submodules=submodules, callbacks=callbacks)
        for submodule_path in submodules:
            submodule = repo.submodules[submodule_path]
            submodule_repo = submodule.open()
            self.init_submodules(external_callbacks=callbacks, repo=submodule_repo)

        if external_callbacks is None:
            callbacks.save()

    def create_tag(self, name, source, base, annotation=None):
        """ create a tag based on HEAD, branch or commit """
        commit_hex = base
        if source is CreateFrom.HEAD:
            commit_hex = str(self.repo.head.target)
        elif source is CreateFrom.BRANCH:
            commit_hex = str(self.repo.branches[base].target)

        if annotation is None:
            self.repo.references.create(f"refs/tags/{name}", commit_hex)
        else:
            self.repo.create_tag(
                name,
                commit_hex,
                pygit2.enums.ObjectType.COMMIT,
                self.repo.default_signature,
                annotation)

    def create_branch(self, name, source, base, checkout=False, force=False):
        """ create a branch based on HEAD, branch or commit """
        commit_hex = base
        if source is CreateFrom.HEAD:
            commit_hex = str(self.repo.head.target)
        elif source is CreateFrom.BRANCH:
            commit_hex = str(self.repo.branches[base].target)

        commit = self.repo.revparse_single(commit_hex)
        self.repo.branches.create(name, commit, force)

        if checkout:
            self.checkout(name, force=force)

    def delete_branch(self, name):
        """ delete a branch by name """
        self.repo.branches.delete(name)

    def delete_reference(self, name):
        """ delete a reference by name """
        head = self.repo.head
        if head.name == name:
            raise RuntimeError("Cannot delete current HEAD")
        self.repo.references.delete(name)

    def get_remotes(self):
        """ get remotes """
        remotes = self.repo.remotes

        return remotes

    def get_remote_url_by_name(self, name):
        """ get urls for remote """
        remote = self.repo.remotes[name]

        return remote.url, remote.push_url

    def update_remote(self, old_name, new_name, url, push_url):
        """ update a remote, if old_name is empty a new remote will be added """
        remotes = self.repo.remotes

        if old_name and len(old_name) > 0:
            if old_name != new_name:
                remotes.rename(old_name, new_name)
            remotes.set_url(new_name, url)
            if push_url is not None and len(push_url) > 0:
                remotes.set_push_url(new_name, push_url)
            else:
                try:
                    remotes.set_push_url(new_name, None)
                except Exception:
                    # we cannot unset an empty push url, ignore exception
                    pass
        else:
            remotes.create(new_name, url)
            if push_url is not None and len(push_url) > 0:
                remotes.set_push_url(new_name, push_url)

    def remove_remote(self, name):
        """ remove remote by name """
        self.repo.remotes.delete(name)

    def get_revision_by_commit(self, hex):
        """ get revision object by commit """
        return self.repo.revparse_single(hex)

    def get_revision_by_branch(self, name):
        """ get revision object by branch name """
        branch = self.repo.branches[name]
        commit_hex = str(branch.target)
        return self.repo.revparse_single(commit_hex)

    def get_submodules(self):
        """ get list of submodules """
        submodules = self.repo.listall_submodules()
        return submodules

    def add_submodule(self, repo, path):
        """ add a new submodule """
        callbacks = TurtleCallbacks()
        self.repo.submodules.add(repo, path, callbacks=callbacks)

        callbacks.save()

    def remove_path(self, path):
        """ remove a path from the index """
        index = self.repo.index
        index.read()
        index.remove(path)
        index.write()

    def get_conflicts(self, _path=None):
        """ get list of conflicts """
        conflicts = []

        if self.repo.index.conflicts is not None:
            for conflict in self.repo.index.conflicts:
                if len(conflict) == 3:
                    conflicts.append((conflict[0], conflict[1], conflict[2]))

        return conflicts

    def get_file_from_current_index(self, path, name):
        """ store content of file from current index into a tmp file and return temp file object """
        try:
            index = self.repo.index[path]
            return self.get_files_from_index(index, name)
        except Exception as _ex:
            pass

        return None

    def get_files_from_index(self, index, name):
        """ store content of file from an index into a tmp file and return temp file object """

        temp = None
        try:
            file_path = index.path.split("/")[-1]
            temp = tempfile.NamedTemporaryFile(suffix=f"__{name}_{file_path}")

            blob = self.repo[index.id]

            temp.write(blob.data)
            temp.flush()
        except Exception:
            if temp:
                temp.close()

        return temp

    def is_merge_in_progress(self):
        """ check if a merge is currently in progress
         if so also return the merge_head """
        merge_path = self.repo.path + "MERGE_HEAD"
        try:
            merge_file = open(merge_path, "r", encoding="utf8")
            if merge_file is not None:
                merge_head = merge_file.readline().strip()
                is_merge = len(merge_head) > 0

                return is_merge, merge_head
        except Exception as _ex:
            pass
        return False, None

    def is_rebase_in_progress(self):
        """ check if a merge is currently in progress
         if so also return the merge_head """
        rebase_path = pathlib.Path(self.repo.path) / "REBASE_HEAD"
        rebase_merge_path = pathlib.Path(self.repo.path) / "rebase-merge"
        try:
            if rebase_merge_path.exists() and rebase_merge_path.is_dir():
                rebase_file = open(rebase_path, "r", encoding="utf8")
                if rebase_file is not None:
                    rebase_head = rebase_file.readline().strip()
                    is_rebase = len(rebase_head) > 0

                    return is_rebase, rebase_head
        except Exception as _ex:
            pass
        return False, None

    def can_be_staged(self, path, raise_ex=False):
        """ check if a file can actually be staged, raises exception if not """
        status, _ = self.get_commit_info(True, False)

        file = self.get_relative_file_path(path)

        if file in status:
            has_wt_status, file_status = turtlevcs.has_worktree_status(status[file])
            if has_wt_status:
                if file_status == pygit2.enums.FileStatus.WT_MODIFIED:
                    return True, False
                if file_status in [
                    pygit2.enums.FileStatus.WT_NEW,
                    pygit2.enums.FileStatus.WT_DELETED]:
                    return True, True

        if raise_ex:
            raise RuntimeError(f"The file '{file}' cannot be staged.")

        # can_stage, new_or_deleted
        return False, False

    def stage_file(self, path):
        """ stage a single file """
        self.repo.index.add(path)
        self.repo.index.write()

    def stage_file_as_index(self, file_path, index_path):
        """ stage contents of a given file as a specific index, i.e. for staging hunks """
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf8") as file:
                file_contents = file.read()
                new_id = self.repo.write(pygit2.enums.ObjectType.BLOB, file_contents)
                index = pygit2.IndexEntry(index_path, new_id, pygit2.enums.FileMode.BLOB)
                self.repo.index.add(index)
                self.repo.index.write()
        else:
            self.repo.index.remove(index_path)
            self.repo.index.write()

    def can_be_reverted(self, file_path, raise_ex=False):
        """ check if a file can actually be reverted """
        status, _ = self.get_commit_info(True, False)

        if file_path in status:
            has_wt_status, wt_status = turtlevcs.has_worktree_status(status[file_path])
            return has_wt_status, wt_status == pygit2.enums.FileStatus.WT_NEW

        if raise_ex:
            raise RuntimeError(f"The file '{file_path}' cannot be staged.")

        return False, False

    def revert(self, file_path):
        """ revert worktree changes for a given file """
        can_be_reverted, wt_new = self.can_be_reverted(file_path)
        if can_be_reverted:
            file = str(self.get_full_file_path(file_path))
            if wt_new:
                os.remove(file)
            else:
                index = self.repo.index
                file_id = index[file_path].id
                blob = self.repo[file_id]

                with open(file, "wb") as file:
                    file.write(blob.data)

    def can_be_unstaged(self, file_path, raise_ex=False):
        """ check if a file can actually be unstaged """
        if os.path.exists(file_path):
            status, _ = self.get_commit_info(False, False)

            file = self.get_relative_file_path(file_path)

            if file in status:
                if turtlevcs.has_index_status(status[file]):
                    return True

        if raise_ex:
            raise RuntimeError(f"The file '{file}' cannot be unstaged.")

        return False

    def unstage(self, file_path):
        """ remove file from index """
        self.repo.index.read()
        self.repo.index.remove(file_path)
        try:
            obj = self.repo.revparse_single('HEAD').tree[file_path]
            self.repo.index.add(pygit2.IndexEntry(file_path, obj.id, obj.filemode))
        except Exception as _ex:
            pass # file might not have been in the last commit
        finally:
            self.repo.index.write()

    def merge(self, branch_name=None, commit_hash=None, ff_only=False, no_ff=False):
        """ merge a branch or commit into the current branch """

        if ff_only and no_ff:
            raise RuntimeError("Cannot use both fast forward only and no fast forward")

        if branch_name.startswith("refs/"):
            branch_name = branch_name.split("/", 2)[-1]

        message = None
        title = None

        merge_head = None
        if branch_name:
            branch = self.repo.branches[branch_name]
            merge_head = branch.target
            merge_head_name = branch_name
        elif commit_hash:
            commit = self.repo.revparse_single(commit_hash)
            merge_head = commit.id
            merge_head_name = commit.short_id

        if merge_head:
            merge_result, _ = self.repo.merge_analysis(merge_head)
            can_ff = (merge_result & pygit2.enums.MergeAnalysis.FASTFORWARD) > 0

            if merge_result & pygit2.enums.MergeAnalysis.UP_TO_DATE:
                # do nothing
                title = "Info"
                message = "Already up to date"

            elif ff_only and not can_ff:
                title = "Error"
                message = "Fast forward not possible"

            elif can_ff:
                if no_ff:
                    merged_index = self.repo.merge_commits(self.repo.head.target, merge_head)
                    self._do_merge_commit(merged_index, merge_head, merge_head_name)
                    # merge_commits does not update the working directory, reset it manually
                    self.repo.checkout_head()
                else:
                    self.repo.checkout_tree(self.repo.get(merge_head))
                    self.repo.head.set_target(merge_head)

            elif merge_result & pygit2.enums.MergeAnalysis.NORMAL:
                if ff_only:
                    title = "Error"
                    message = "No fast forward possible"
                else:
                    self.repo.merge(merge_head, pygit2.enums.MergeFavor.NORMAL)

                    if self.repo.index.conflicts is None:
                        self._do_merge_commit(self.repo.index, merge_head, merge_head_name)
                    else:
                        title = "Conflicts"
                        message = "Fix conflicts and then commit the result"

        return message, title

    def _do_merge_commit(self, index, merge_head, merge_head_name):
        signature = turtlevcs.get_author(self.repo)
        tree = index.write_tree()
        self.repo.create_commit(
            "HEAD",
            signature,
            signature,
            f"Merge '{merge_head_name}' into {self.repo.head.shorthand}",
            tree,
            [self.repo.head.target, merge_head])
        self.repo.state_cleanup()

    def reset(self, commit_hash, mode):
        """ reset the current branch to a specific commit """
        commit = self.repo.revparse_single(commit_hash)
        self.repo.reset(commit.id, mode)

    def clean(self, non_ignored=True, ignored=True, directories=False, dry_run=False):
        """ clean a repository """
        cleaned_files = []

        status = self.repo.status(
            untracked_files="all", ignored=ignored)

        for p, s in status.items():
            match_new = s == pygit2.enums.FileStatus.WT_NEW and non_ignored
            match_ignore = s == pygit2.enums.FileStatus.IGNORED and ignored
            path = pathlib.Path(self.get_full_file_path(p))
            match_directory = directories and path.is_dir()
            is_file = path.is_file()

            if is_file or match_directory:
                if match_new or match_ignore:
                    if not dry_run:
                        if path.is_dir():
                            shutil.rmtree(path)
                        elif path.is_file():
                            path.unlink()
                    cleaned_files.append(p)

        return cleaned_files


def clone(url, path, recursive, bare, progress_callback):
    """ clone repository from url into local path """
    callbacks = TurtleCallbacks(progress_callback)
    new_repo = pygit2.clone_repository(url, path, bare, callbacks=callbacks)

    callbacks.save()

    if recursive:
        # TODO not tested yet
        turtle = Turtle(path)
        turtle.init_submodules()

    return new_repo

def init(path, bare):
    """ init a new repo """
    repo = pygit2.init_repository(
        path,
        bare,
        pygit2.enums.RepositoryInitFlag.MKPATH | pygit2.enums.RepositoryInitFlag.NO_REINIT)
    return repo

def sign_message(message, gpg_key=None, _gpg_password=None) -> str:
    """ sign a message with seahorse """
    # pylint: disable=C0415
    import dbus
    # pylint: enable=C0415
    bus = dbus.SessionBus()
    seahorse = bus.get_object('org.gnome.seahorse', '/org/gnome/seahorse/crypto')
    crypto = dbus.Interface(seahorse, 'org.gnome.seahorse.CryptoService')

    if gpg_key:
        gpg_key = f"openpgp:{gpg_key}"
    else:
        seahorse = bus.get_object('org.gnome.seahorse', '/org/gnome/seahorse/keys/openpgp')
        keys = dbus.Interface(seahorse, 'org.gnome.seahorse.Keys')
        keys = keys.ListKeys()

        for key in keys:
            key_string = str(key)
            has, value = keys.GetKeyField(key, "flags")
            if has:
                flag = int(value)
                if flag & 4 > 0:
                    gpg_key = key_string
                    break

    if gpg_key is None:
        raise RuntimeError("no gpg key available")

    signed = crypto.SignText(gpg_key, 0, message)

    signed_message = str(signed)
    pos = signed_message.find("-----BEGIN PGP SIGNATURE-----")
    signed_message = signed_message[pos:]

    return signed_message

def verify_message(message, signed_message):
    """ verify signed message with seahorse """
    # pylint: disable=C0415
    import dbus
    # pylint: enable=C0415
    bus = dbus.SessionBus()
    seahorse = bus.get_object('org.gnome.seahorse', '/org/gnome/seahorse/crypto')
    crypto = dbus.Interface(seahorse, 'org.gnome.seahorse.CryptoService')

    full_signed_message = (
        "-----BEGIN PGP SIGNED MESSAGE-----\nHash: SHA512\n\n" +
        message + "\n" +
        signed_message)

    _verified, signer = crypto.VerifyText("openpgp", 1, full_signed_message)

    return signer
