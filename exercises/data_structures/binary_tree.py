# Node class
class node(object):

    # initialize node object (contains value and left and right children)
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

    # prints recursively in tree shape
    def print(self, level=0):
        if(self.right != None):
            self.right.print(level + 1)
        print("\t" * level + repr(self.value))
        if(self.left != None):
            self.left.print(level + 1)

    # insert new node
    def insert(self, new):
        print(f"FIXME: Insert a node")
        return(-1)
