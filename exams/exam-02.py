# dependencies
import random

# Q1:
# Given a doubly linked list, write an insert function and delete function. An
# implementation for a DoubleLink is provided below. Do not use any extra lists,
# dictionaries, or any extra data structures to solve this problem.
class DoubleLink(object):
    # DO NOT MODIFY
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    # handle str representation
    def __str__(self):
        return(f"{self.data}")

class DoublyLinkedList(object):
    # initialize doubly linked list, head takes a DoubleLink 
    def __init__(self, head=None):
        self.head = self.tail = head

    # handle str representation
    def __str__(self):
        if(self.head == None):
            return("")
        current = self.head 
        str_links = ""
        str_connect = " -> "
        while(current != None):
            str_links += f"{current}{str_connect}"
            current = current.next
        return(str_links[:-len(str_connect)])

    # insert in ascending order without using any extra data structures
    def insert_in_order(self, data):
        new = DoubleLink(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            prev = current = self.head
            while(data >= current.data):
                prev = current
                current = current.next
                if(current == None):
                    prev.next = new
                    new.prev = prev
                    self.tail = new
                    return
            if(current == self.head):
                new.next = current
                current.prev = new
                self.head = new
            else:
                new.next = current
                new.prev = prev
                current.prev = new
                prev.next = new
    
    # delete a link from the list (that may or may not be there)
    def delete(self, data):
        if(self.head == None):
            return(None)
        current = self.head 
        while(current.data != data):
            current = current.next
            if(current == None):
                return(None)
        if(current == self.head):
            self.head = self.head.next
            if(current == self.tail):
                self.tail = None
        elif(current == self.tail):
            self.tail = self.tail.prev
        else:
            prev = current.prev
            current.next.prev = prev
            prev.next = current.next
        return(current)

# Q2:
# Q3:
# Q4:
# Q5:
# EC:

def main():
    # Q1 - Doubly Linked List
    print(f"Q1: Doubly Linked List Implementation")
    size = 10
    myList = DoublyLinkedList()
    [myList.insert_in_order(random.randint(-size, size)) for i in range(size)]
    print(myList)

main()