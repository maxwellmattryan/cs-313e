#  File: TestLinkedList.py

#  Description: Assignment 16 | Singly Linked List

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10-28-2019

#  Date Last Modified: 10-28-2019

class Link (object):
    # initialize link object
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    # handles str representation
    def __str__(self):
        return(f"{self.data}")

class LinkedList (object):
    # initializion of linked list object
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    # get number of links 
    def get_num_links (self):
        return(self.length)

    # add an item at the beginning of the list
    def insert_first (self, data): 
        self.length += 1
        new = Link(data)
        new.next = self.head
        self.head = new
        if(self.tail == None):
            self.tail = new

    # add an item at the end of a list
    def insert_last (self, data): 
        self.length += 1
        new = Link(data)
        if(self.tail != None):
            self.tail.next = new
        self.tail = new
        if(self.head == None):
            self.head = new

    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 
        ...

    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        ...

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        ...

    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        ...

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        wholeString = ""
        lineItems = []
        current = self.head
        while(current != None):
            lineItems.append(str(current.data))
            if(len(lineItems) == 10):
                wholeString += f"{'  '.join(lineItems)}\n"
                lineItems = []
            current = current.next
        return(wholeString + '  '.join(lineItems))

    # Copy the contents of a list and return new list
    def copy_list (self):
        ...

    # Reverse the contents of a list and return new list
    def reverse_list (self): 
        ...

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self): 
        ...

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        ...

    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        ...

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other): 
        ...

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        ...

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        ...

def main():
    # Test methods insert_first() and __str__() by adding more than 10 items to a list and printing it.
    myList = LinkedList()
    [myList.insert_first(i + 1) for i in range(12)]
    print(f"{myList}\nHead = {myList.head}, Tail = {myList.tail}, Length = {myList.length}\n")

    # Test method insert_last()
    myList = LinkedList()
    [myList.insert_last(i + 1) for i in range(17)]
    print(f"{myList}\nHead = {myList.head}, Tail = {myList.tail}, Length = {myList.length}\n")

    # Test method insert_in_order()

    # Test method get_num_links()

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 

    # Test method delete_link()
    # Consider two cases - data is there, data is not there 

    # Test method copy_list()

    # Test method reverse_list()

    # Test method sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()

if __name__ == "__main__":
    main()