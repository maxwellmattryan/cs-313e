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

class Queue(object):
    # initialize queue object
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    
    # add to the queue
    def enqueue(self, value):
        new = Node(value)
        if(self.head == None):
            self.head = new
        else:
            self.tail.next = new
            new.previous = self.tail
        self.tail = new
    
    # remove from the queue
    def dequeue(self):
        target = self.head
        self.head = self.head.next
        self.head.previous = None
        return(target)