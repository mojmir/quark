__author__ = 'planck'

import os


class Listener:
    """
    Class for providing commands to tree structure and simple movement in it.

    Should provide way how to get input to QuarkTree. Command should be always
    performed in file tree in directory which working quark represents,

    Attributes:
        quark_tree: QuarkTree object to which we provide commands
        working_quark: Quark object, active quark in the tree.
    """
s
    def __init__(self, quark_tree):
        """
        Constructor
        """
        self.quark_tree = quark_tree
        self.working_quark = quark_tree.working_quark

    def change(self, name):
        """
        Tries to go to subdirectory of the selected name in QuarkTree.

        Changes working quark to one of the quarks which are in the branches.
        If there are no quarks in the branches grows the quark. If there is
        no such quark with selected error raises NameError exception.

        Args:
            name: quark branch name (subfolder) to change working quark

        Raises
            NameError: Unknown quark name of branch which can't be found
        """
        for little_branch in self.working_quark.branches:
            if little_branch.base_name == name:
                self.working_quark = little_branch
                break
        else:
            raise NameError(("Unknown quark: " + str(name)))

        if not self.working_quark.branches:
            self.working_quark.grow()

    def change_directory(self, directory, show=False):
        """
        Changes working directory according to relative path.

        Splits difference between required directory absolute path and
        root of the QuarkTree directory and follows it via change function

        Args:
            directory: string, relative path to the new working directory
            show: bool, should be tree displayed

        """
        os.chdir(directory)
        absolute = os.path.abspath(os.curdir)
        master_dir = self.quark_tree.master_dir
        self.working_quark = self.quark_tree.root
        relative = absolute.replace(master_dir, "")[1:]

        for level in relative.split(os.path.sep):
            self.change(level)

        if show:
            self.quark_tree.show(
                self.quark_tree.root,
                ""
            )