#lmao help
# This seems like it should probably be some kind of recursive solution
def filehander (f):
    instructions = []
    for line in f:
        # ok
        line.split(")")
        instructions.append(line[0],line[1])
    return instructions

# this also might require some kind of list-like data structure
# I have no idea how to write classes in python LMAO
# I also don't want to make a data structure

def sort(ins):
    nds = {}
    nodes = []
    for x in ins:
        nds.add(x[1])
    for x in nds:
        nodes.append(Node(x))
# what I want to do :
# find root,
# find things branching from root
# give every object a distance_from_root type deal
class Node():
    data = ""
    orbits = ''
    def __init__(self,data=None,orbits =None)
        self.data = data
        self.orbits = orbits


class NodeSet(Node):
    pass
