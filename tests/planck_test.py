__author__ = 'planck'

from lib.listener import Listener
from lib.quarktree import QuarkTreess

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