__author__ = 'planck'

import os
import glob


class Quark:
    """
    Represents file or directory as nod for Tree structure.

    Attributes:
        base_name: quark name, name of the directory, file it represents
        path: absolute path to the directory which quark represents
        branches: list of the quarks which represents subfolders
        level: how deep is quark from the root
        is_dir: bool, does quark represent directory

    Methods:
        grow: if quark represents directory. creates representative quarks for
            all subfolders and files in it and stores them as branches
        branch_names: returns, tuple of branch base_names
    """

    def __init__(self, path, name, level):
        """
        Constructor
        """
        self.base_name = name
        self.path = path
        self.isdir = os.path.isdir(name)

        if self.isdir:
            self.branches = []
        #self.parent = parent
        #TODO check if I will need a parents :)
        self.level = level + 1

    def grow(self):
        """
        Loads subfolders, files quark representatives into branches.

        if quark represents directory. creates representative quarks for all
        subfolders and files in it and stores them as branches.
        """
        print "Growing " + self.base_name
        print str(self.path + os.path.sep + self.base_name)

        if self.isdir:
            full_path = self.path + os.path.sep + self.base_name
            os.chdir(full_path)

            for item in glob.glob("*"):
                if item not in self.branch_names():
                    self.branches.append(Quark(full_path, item, self.level))

    def branch_names(self):
        """
        Creates set of branches base_names and returns it.

        Returns:
            Tuple, with each branch base_names
        """
        if self.branches:
            names = (branch_name.base_name for branch_name in self.branches)
            return names
        return ()


