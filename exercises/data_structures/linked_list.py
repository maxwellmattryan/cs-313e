# DATA STRUCTURES
# Linked List, Doubly-Linked List, and Circularly-Linked List
# Each uses the Link class, even though singly-linked and circul-
# arly-linked lists don't use pointers to the previous link.

# Links
class Link(object):
    # initialization of link
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    # handle self as print argument
    def __str__(self):
        return(f"{self.data}")

# Linked Lists (insert, remove)
class LinkedList(object):
    # initialization of linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # handles len calling
    def __len__(self):
        return(self.length)

    # handle self as print argument 
    def __str__(self):
        current = self.head
        itemString = ""
        while(current != None):
            if(current.next == None):
                return(itemString + str(current))
            itemString += f"{current}, "
            current = current.next
        return(itemString)

    # appending a link
    def append(self, data):
        self.length += 1
        new = Link(data)
        if(self.tail == None or self.head == None):
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    # insert a link before element at specified index (default)
    def insert(self, data, index):
        self.length += 1
        new = Link(data)
        current = self.head
        counter = 0
        while(current != None):
            if(counter + 1 == index):
                new.next = current.next
                current.next = new
                current = new
                break
            counter += 1
            current = current.next

    # insert a link after an element at a specific index
    def insertAfter(self, data, index):
        self.length += 1
        new = Link(data)
        if(index == self.length - 1):
            self.tail.next = new
            self.tail = new
        elif(index < self.length - 1):
            current = self.head
            counter = 0
            while(current != None):
                if(counter == index):
                    new.next = current.next
                    current.next = new
                counter += 1
                current = current.next

    # returns the value at the given index
    def get(self, index):
        counter = 0
        current = self.head
        while(current != None):
            if(counter == index):
                return(current.data)
            counter += 1
            current = current.next

    # return maximum value in linked list
    def maximum(self):
        current = self.head
        maximum = current.data
        while(current != None):
            if(current.data > maximum):
                maximum = current.data
            current = current.next
        return(maximum)

    # return minimum value in linked list
    def minimum(self):
        current = self.head
        minimum = current.data
        while(current != None):
            if(current.data < minimum):
                minimum = current.data
            current = current.next
        return(minimum)
    
    # prepending a link
    def prepend(self, data):
        self.length += 1
        new = Link(data)
        if(self.tail == None):
            self.tail = new
        else:
            new.next = self.head
        self.head = new

    # removing the first link that matches the target
    def remove(self, target):
        self.length -= 1
        current = self.head
        if(current.data == target):
            self.head = self.head.next
        else:
            while(current.next != None):
                if(current.next.data == target):
                    current.next = current.next.next
                    if(current.next == None):
                        self.tail = current
                    break
                current = current.next

    # remove the link at the specified index
    def removeAt(self, index):
        self.length -= 1
        current = self.head
        counter = 0
        while(current != None):
            if(counter + 1 == index):
                if(current.next.next == self.tail):
                    self.tail = current.next
                current.next = current.next.next
                break
            counter += 1
            current = current.next

    # reverses the list
    def reverse(self):
        previous = self.head
        current = previous.next
        previous.next = None
        self.head = previous
        while(current != None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    # searches for the target element, returns index if found, -1 otherwise
    def search(self, target):
        index = 0
        current = self.head
        while(current != None):
            if(current.data == target):
                return(index)
            index += 1
            current = current.next

    # sorts the list using insertion sort
    def sort(self, reverse=False):
        print(f"FIXME: sort()")
        return(-1)