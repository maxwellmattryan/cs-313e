# Node class
class node(object):
    
    # initialize node object
    def __init__(self, data=0):
        self.data = data
        self.next = None
    
    # format node object printing
    def __str__(self):
        return(f"{self.data}")

# Linked List class
class linked_list(object):

    # initialize linked list object
    def __init__(self):
        self.head = None
        self.tail = None

    # handles len() calls => 0(n)
    def __len__(self):
        count = 0
        current = self.head
        while(current != None):
            count += 1
            current = current.next
        return(count)

    # handles print() calls
    def __str__(self):
        return(str(self.print(True, True)))

    # append a new tail node => O(1)
    def append(self, new):
        if(self.head == None):
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
    
    # clear all elements from list => O(1)
    def clear(self):
        self.head = self.tail = None

    # gets node at given index => O(n)
    def get(self, index):
        self.print()
        current = self.head
        while(index > 0):
            if(current.next == None):
                return(None)
            current = current.next
            index -= 1
        return(current)

    # gets index of node whose data equals key => O(n)
    def index_of(self, key):
        current = self.head
        index = 0
        while(current != None):
            if(current.data == key):
                return(index)
            else:
                index += 1
                current = current.next
        return(-1)

    # insert new node after target node => O(n)
    def insert(self, new, target):
        # empty list
        if(self.head == None):
            self.head = new
            self.tail = new
        # if target is list's tail node
        elif(target == self.tail):
            self.tail.next = new
            self.tail = new
        # target is in middle of list
        else:
            new.next = target.next
            target.next = new

    # prepend a new head node => O(1)
    def prepend(self, new):
        if(self.head == None):
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new
    
    # print values of linked list in list format (by default) => O(n)
    def print(self, print_list=True, return_list=False):
        data = []
        current = self.head
        while(current != None):
            if(not print_list):
                print(current)
            data.append(current.data)
            current = current.next
        if(return_list):
            return(data)
        if(print_list):
            print(data)

    # print values of linked list recursively (one value per line) => O(n)
    def print_recursive(self, current):
        if(current != None):
            print(current)
            self.print_recursive(current.next)

    # remove the node after the given node => O(n)
    def remove(self, target):
        if(target == None and self.head != None):
            next = self.head.next
            self.head = next
            if(next == None):
                self.tail = None
        elif(target.next != None):
            next = target.next.next
            target.next = next
            if(next == None):
                self.tail = target

    # reverse a linked list => O(n)
    def reverse(self):
        previous = self.head
        current = previous.next
        previous.next = None
        self.tail = previous
        while(current != None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    # sort the linked list by insertion sort => O(n^2)
    def sort(self, reverse=False):
        # find correct index to insert current node
        def find_insert_pos(self, data):
            nodeA = None
            nodeB = self.head
            while(nodeB != None and data > nodeB.data):
                nodeA = nodeB
                nodeB = nodeB.next
            return(nodeA)
        before = self.head
        current = before.next
        while(current != None):
            next = current.next
            position = find_insert_pos(self, current.data)
            if(position == before):
                before = current
            else:
                self.remove(before)
                if(position == None):
                    self.prepend(current)
                else:
                    self.insert(current, position)
            current = next
        if(reverse):
            self.reverse()