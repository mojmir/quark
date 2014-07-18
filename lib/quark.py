__author__ = 'planck'

import os
import glob


class Quark:
    """
    Represents file or directory as nod for Tree structure.
    """
    def __init__(self, path, name, level):
        self.base_name = name
        self.path = path
        self.branches = []
        #self.parrent = parent
        self.level = level + 1
        self.isdir = os.path.isdir(name)

    def grow(self):
        print "Growing " + self.base_name
        print str(self.path + os.path.sep + self.base_name)
        if self.isdir:
            full_path = self.path + os.path.sep + self.base_name
            os.chdir(full_path)
            print str(glob.glob("*"))
            for item in glob.glob("*"):
                if item not in self.branch_names():
                    self.branches.append(Quark(full_path, item, self.level))


    def branch_names(self):
        names = [branch_name.base_name for branch_name in self.branches]
        return names


class QuarkTree:
    """
    Tree structure with quarks as nods.
    """
    #TODO Check python inheriting from quark possibility
    def __init__(self, working_dir=os.curdir):
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
        absolute = os.path.abspath(os.curdir)
        quarks = [
            Quark(absolute, item, self.deepness) for item in glob.glob("*")
        ]
        return quarks

    def show(self, quark, name):
        new_name = name[:]
        if quark.branches:
            new_name += "  +" + quark.base_name
            for local_branch in quark.branches:
                self.show(local_branch, new_name)
        else:
            if quark.isdir:
                new_name += "  +" + quark.base_name
                print new_name
            else:
                new_name += "  -" + quark.base_name
                print new_name


class Listener:
    def __init__(self, quark_tree):
        self.quark_tree = quark_tree
        self.working_quark = quark_tree.working_quark

    def change(self, name):
        print "working quark is " + self.working_quark.base_name
        for little_branch in self.working_quark.branches:
            if little_branch.base_name == name:
                self.working_quark = little_branch
                break
        else:
            raise NameError(("Unknown quark: " + str(name)))

        if not self.working_quark.branches:
            self.working_quark.grow()

    def change_directory(self, directory):
        os.chdir(directory)
        absolute = os.path.abspath(os.curdir)
        master_dir = self.quark_tree.master_dir
        self.working_quark = self.quark_tree.root
        relative = absolute.replace(master_dir, "")[1:]
        print "            Abslotue path is:  " + absolute
        print "Working directory of tree is:  " + master_dir
        print "            Relative name is:  " + relative

        for level in relative.split(os.path.sep):
            print "level is " + level
            self.change(level)

        self.quark_tree.show(
            self.quark_tree.root,
            ""
        )


tree = QuarkTree("/home/planck/PycharmProjects")
tree.show(tree.root, "")
listener = Listener(tree)

print "Changing directory"
listener.change_directory("./quark")

print "working quark is " + listener.working_quark.base_name
print "It is directory: " + str(listener.working_quark.isdir)

print "Its branches are: "
listener.working_quark.grow()
for branch in listener.working_quark.branches:
    print "Branch is " + str(branch.base_name)


listener.change_directory("./first_design")
print "It is directory: " + str(listener.working_quark.isdir)
print "Working directory"

"""
for branch in a.root.branches:
    branch.grow()

print 'After bloom.'

a.show_tree(a.root, "")
"""