import os
from functools import cached_property
from typing import Self, override

from codeowners import CodeOwners as CodeOwnersParser
from git import Remote
from git import Repo as GitCLI
from git.remote import PushInfoList

from codegen.utils.codemod.codemod_writer_decorators import noapidoc
from codegen.utils.file_io.create import create_files
from graph_sitter.output.utils import url_to_github

from .repo_operator import RepoOperator
from .schemas.config import BaseRepoConfig
from .schemas.enums import FetchResult


class OperatorIsLocal(Exception):
    """Error raised while trying to do a remote operation on a local operator"""


class LocalRepoOperator(RepoOperator):
    """RepoOperator that does not depend on remote Github.
    It is useful for:
    - Testing codemods locally with a repo already cloned from Github on disk.
    - Creating "fake" repos from a dictionary of files contents
    """

    _repo_path: str
    _repo_name: str
    _default_branch: str
    _git_cli: GitCLI
    repo_config: BaseRepoConfig

    def __init__(
        self,
        repo_config: BaseRepoConfig,
        repo_path: str,  # full path to the repo
        default_branch: str,  # default branch of the repo
        bot_commit: bool = True,
    ) -> None:
        self._repo_path = repo_path
        self._repo_name = os.path.basename(repo_path)
        self._default_branch = default_branch
        os.chdir(self.repo_path)
        os.makedirs(self.repo_path, exist_ok=True)
        GitCLI.init(self.repo_path)
        super().__init__(repo_config, self.repo_path, bot_commit)

    ####################################################################################################################
    # CLASS METHODS
    ####################################################################################################################
    @classmethod
    def create_from_files(cls, repo_path: str, files: dict[str, str], bot_commit: bool = True, repo_config: BaseRepoConfig = BaseRepoConfig()) -> "LocalRepoOperator":
        """Used when you want to create a directory from a set of files and then create a LocalRepoOperator that points to that directory.
        Use cases:
        - Unit testing
        - Playground
        - Codebase eval

        Args:
            repo_path (str): The path to the directory to create.
            files (dict[str, str]): A dictionary of file names and contents to create in the directory.
            repo_config (BaseRepoConfig): The configuration of the repo.
        """
        # Step 1: Create dir (if not exists) + files
        os.makedirs(repo_path, exist_ok=True)
        create_files(base_dir=repo_path, files=files)

        # Step 2: Init git repo
        op = cls(repo_path=repo_path, default_branch="main", bot_commit=bot_commit, repo_config=repo_config)
        if op.stage_and_commit_all_changes("[Codegen] initial commit"):
            op.checkout_branch(op.default_branch, create_if_missing=True)
        return op

    @classmethod
    def create_from_commit(cls, repo_path: str, default_branch: str, commit: str, url: str) -> Self:
        """Do a shallow checkout of a particular commit to get a repository from a given remote URL."""
        op = cls(repo_config=BaseRepoConfig(), repo_path=repo_path, default_branch=default_branch, bot_commit=False)
        if op.get_active_branch_or_commit() != commit:
            op.discard_changes()
            op.create_remote("origin", url)
            op.git_cli.remotes["origin"].fetch(commit, depth=1)
            op.checkout_commit(commit)
        return op

    ####################################################################################################################
    # PROPERTIES
    ####################################################################################################################

    @property
    def repo_name(self) -> str:
        return self._repo_name

    @property
    def repo_path(self) -> str:
        return self._repo_path

    @property
    def codeowners_parser(self) -> CodeOwnersParser | None:
        return None

    @cached_property
    @noapidoc
    def base_url(self) -> str | None:
        if remote := next(iter(self.git_cli.remotes), None):
            return url_to_github(remote.url, self.get_active_branch_or_commit())

    @override
    def push_changes(self, remote: Remote | None = None, refspec: str | None = None, force: bool = False) -> PushInfoList:
        raise OperatorIsLocal()

    @override
    def pull_repo(self) -> None:
        """Pull the latest commit down to an existing local repo"""
        raise OperatorIsLocal()

    def fetch_remote(self, remote_name: str = "origin", refspec: str | None = None, force: bool = True) -> FetchResult:
        raise OperatorIsLocal()
