# stack class (implemented in doubly-liunked list)
class Node(object):
    # initialize node object
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.previous = None
    
    # handle printing
    def __str__(self):
        return(f"{self.value}")

class Stack(object):
    # initialize stack class
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    # handles printing
    def __str__(self):
        current = self.head
        while(current != None):
            print(current, end=" ")
            current = current.next
        return("")

    # only return top element
    def peek(self):
        return(self.tail)

    # define a pop method
    def pop(self):
        if(self.tail != None):
            popped = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            return(popped)
        return

    # define push method
    def push(self, value):
        new = Node(value)
        if(self.head == None):
            self.head = new
            self.head.next = self.head.previous = None
        else:
            new.previous = self.tail
            self.tail.next = new
        self.tail = new