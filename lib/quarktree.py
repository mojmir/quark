__author__ = 'planck'

import glob
import os

from lib.quark import Quark


class QuarkTree:
    """
    Quark tree structure representing file system. With quark root.

    Should included all operation on quark tree which have to be global, mostly
    recursive functions for reloading tree its displaying and tree changes.

    Attributes:
        deepness: integer, number of levels of tree
        master_dir: string, absolute path to directory where tree starts
        root: Quark, root of the quark tree
        working_quark: Quark (pointer), on quark where commands are placed

    """
    #TODO Check python inheriting from quark possibility

    def __init__(self, working_dir=os.curdir):
        """
        Constructor.

        Raises:
            NameError: If provided path for working dir is not directory.
        """
        self.deepness = 0

        if os.path.isdir(working_dir):
            self.master_dir = working_dir
            absolute = os.path.abspath(working_dir)
            working_dir = absolute.split(os.path.sep)[-1]
            self.root = Quark(absolute, working_dir, 0)
            os.chdir(absolute)
        else:
            raise NameError("Provided path is not directory")

        self.working_quark = self.root
        self.root.branches = self.initial_grow()

    def initial_grow(self):
        """
        Iniatial loading of subfolders, files into the root quark.

        Returns:
            list, Quarks representatives of subfolders and files of root
            directory
        """
        #TODO WHY DIDN'T I USE Quark.Grow()?
        absolute = os.path.abspath(os.curdir)
        quarks = [
            Quark(absolute, item, self.deepness) for item in glob.glob("*")
        ]
        return quarks

    def show(self, quark, quark_path):
        """
        Displays selected quark if it didn't grow yet with it complete
        path of parent quarks.

        Args:
            quark: working quark
            quark_path: list of parents quark to print it reaches end-Quark
        """
        new_quark_path = quark_path[:]

        if quark.branches:
            new_quark_path += "  +" + quark.base_name
            for local_branch in quark.branches:
                self.show(local_branch, new_quark_path)
        else:
            if quark.isdir:
                new_quark_path += "  +" + quark.base_name
                print new_quark_path
            else:
                new_quark_path += "  -" + quark.base_name
                print new_quark_pathvvvvvvvvvvvvs