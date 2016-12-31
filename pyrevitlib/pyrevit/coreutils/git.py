"""
Description:
LibGit2Sharp wrapper module for pyRevit.

Documentation:
https://github.com/libgit2/libgit2sharp/wiki
"""

import clr
import importlib
import os.path as op

# noinspection PyUnresolvedReferences
import System

from pyrevit.coreutils.logger import get_logger

GIT_LIB = 'LibGit2Sharp'

# todo: figure out how to import extensions on the caller's scope.
clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)
clr.AddReferenceByName(GIT_LIB)


logger = get_logger(__name__)


# public libgit module
libgit = importlib.import_module(GIT_LIB)


class RepoInfo:
    """
    Generic repo wrapper for passing repository information to other modules

    """
    def __init__(self, repo):
        self.directory = repo.Info.WorkingDirectory
        self.name = op.basename(op.normpath(self.directory))
        self.head_name = repo.Head.Name
        self.last_commit_hash = repo.Head.Tip.Id.Sha
        self.repo = repo

    def __repr__(self):
        return '<type \'RepoInfo\' head \'{}\' @ {}>'.format(self.last_commit_hash, self.directory)


def get_repo(repo_dir):
    """

    Args:
        repo_dir:

    Returns:
        RepoInfo:
    """
    repo = libgit.Repository(repo_dir)
    return RepoInfo(repo)