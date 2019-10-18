# Node class
class node(object):

    # initialize node object (contains value and left and right children)
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0 # updated when node is found, used only for printing

    # handles print formatting of node object
    def __str__(self):
        return(f"{self.value}, {self.height}")

    # find a given key in a tree
    def find(self, key):
        current = self
        h = 0
        while(current != None):
            if(key == current.value):
                current.height = h
                return(current)
            elif(key < current.value):
                current = current.left
            else:
                current = current.right
            h += 1
        return(-1)

    # insert new node
    def insert(self, new):
        current = self
        if(current == None):
            current = node(new.value)
        else:
            while(current != None):
                if(new.value < current.value):
                    if(current.left == None):
                        current.left = new
                        current = None
                    else:
                        current = current.left
                else:
                    if(current.right == None):
                        current.right = new
                        current = None
                    else:
                        current = current.right
            new.left = None
            new.right = None

    # prints recursively in tree shape
    def print(self, level=0):
        if(self.right != None):
            self.right.print(level + 1)
        print("\t" * level + repr(self.value))
        if(self.left != None):
            self.left.print(level + 1)

    # remove a node from the tree
    def remove(self, key):
        parent = None
        current = self
        while(current != None):
            if(current.value == key):
                if(not current.left and not current.right):
                    if(not parent):
                        self = None
                    elif(parent.left == current):
                        parent.left = None
                    else:
                        parent.right = None
                elif(current.left and not current.right):
                    if(not parent):
                        self = current.left
                    elif(parent.left == current):
                        parent.left = current.left
                    else:
                        parent.right = current.left
                elif(not current.left and current.right):
                    if(not parent):
                        self = current.right
                    elif(parent.left == current.right):
                        parent.left = current.right
                    else:
                        parent.right = current.right
                else:
                    successor = current.right
                    while(successor != None):
                        successor = successor.left
                    current.value = successor.value
                    self.remove(successor.key)
                return
            parent = current
            if(key < current.value):
                current = current.left
            else:
                current = current.right
        return
