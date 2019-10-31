#  File: TestLinkedList.py

#  Description: Assignment 16 | Singly Linked List

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10-28-2019

#  Date Last Modified: 10-30-2019

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

    # prepend an item at the beginning of the list
    def insert_first (self, data): 
        self.length += 1
        new = Link(data)
        new.next = self.head
        if(self.head == None):
            self.tail = new
        self.head = new

    # append an item at the end of a list
    def insert_last (self, data): 
        self.length += 1
        new = Link(data)
        if(self.tail != None):
            self.tail.next = new
        else:
            self.head = new
        self.tail = new

    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            current = self.head
            prev = current
            while(current.data < data):
                prev = current
                current = current.next
                if(current == None):
                    self.tail.next = new 
                    self.tail = new
                    break
            if(current == self.head):
                self.head = new
            else:
                prev.next = new 
            new.next = current

    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        if(self.head == None):
            return(None)
        current = self.head
        while(current.data != data):
            current = current.next
            if(current == None):
                return(None)
        return(current)

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        if(self.head == None):
            return(None)
        current = self.head
        while(current.data != data):
            if(current.data > data):
                return(None)
            current = current.next
            if(current == None):
                return(None)
        return(current)

    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        self.length -= 1
        if(self.head == None):
            return(None)
        elif(self.head.data == data):
            self.head = self.head.next
        current = prev = self.head
        while(current.data != data):
            prev = current
            current = current.next
            if(current == None):
                return(None)
        if(current == self.tail):
            self.tail = prev
        prev.next = current.next
        return(current)

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        wholeString = ""
        if(self.head == None):
            return("None")
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
        newList = LinkedList()
        if(self.head == None):
            return(None)
        current = self.head
        while(current != None):
            newList.insert_last(current.data)
            current = current.next
        return(newList)

    # Reverse the contents of a list and return new list
    def reverse_list (self): 
        if(self.head == None):
            return(None)
        newList = LinkedList()
        current = self.head
        while(current != None):
            newList.insert_first(current.data)
            current = current.next
        return(newList)

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self, reverse=False): 
        if(self.head == None):
            return(None)
        newList = LinkedList()
        current = self.head
        while(current != None):
            newList.insert_in_order(current.data)
            current = current.next
        if(reverse):
            return(newList.reverse_list())
        return(newList)

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        if(self.length < 2):
            return(True)
        current = next = self.head
        while(next != None):
            if(next.data < current.data):
                return(False)
            current = next
            next = next.next
        return(True)

    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        return(self.head == None)

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other): 
        if(self.head == other.head == None):
            return(None)
        newList = LinkedList()
        ptr1 = self.head
        ptr2 = other.head
        while(ptr1 != None and ptr2 != None):
            if(ptr1.data < ptr2.data):
                newList.insert_last(ptr1.data)
                ptr1 = ptr1.next
            else:
                newList.insert_last(ptr2.data)
                ptr2 = ptr2.next
        while(ptr1 != None):
            newList.insert_last(ptr1.data)
            ptr1 = ptr1.next
        while(ptr2 != None):
            newList.insert_last(ptr2.data)
            ptr2 = ptr2.next
        return(newList)

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        if(self.head == other.head == None):
            return(True)
        ptr1 = self.head
        ptr2 = other.head
        while(ptr1 != None and ptr2 != None):
            if(ptr1.data != ptr2.data):
                return(False)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return(True)

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        if(self.head == None):
            return(None)
        current = self.head
        newList = LinkedList()
        while(current != None):
            if(newList.find_unordered(current.data) == None):
                newList.insert_last(current.data)
            current = current.next
        return(newList)

def main():
    # dependencies
    import random

    # Test methods insert_first() and __str__() by adding more than 10 items to a list and printing it.
    myList = LinkedList()
    [myList.insert_first(i + 1) for i in range(12)]
    print(f"Test 01: insert_first() =>\n{myList}\nHead = {myList.head}, Tail = {myList.tail}, Length = {myList.length}\n")

    # Test method insert_last()
    myList = LinkedList()
    [myList.insert_last(i + 1) for i in range(17)]
    print(f"Test 02: insert_last() =>\n{myList}\nHead = {myList.head}, Tail = {myList.tail}, Length = {myList.length}\n")

    # Test method insert_in_order()
    myList = LinkedList()
    [myList.insert_in_order(i) for i in range(24)]
    print(f"Test 03: insert_in_order() =>\n{myList}\nHead = {myList.head}, Tail = {myList.tail}, Length = {myList.length}\n")

    # Test method get_num_links()
    print(f"Test 04: get_num_links() => {myList.get_num_links()}\n")

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    print(f"Test 05a: find_unordered(12) in \n{myList} => {myList.find_unordered(12)}")
    print(f"Test 05b: find_unordered(12_000) in \n{myList} => {myList.find_unordered(12_000)}\n")

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 
    print(f"Test 06a: find_ordered(12) in \n{myList} => {myList.find_ordered(12)}")
    print(f"Test 06b: find_ordered(12_000) in \n{myList} => {myList.find_ordered(12_000)}\n")

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    linkToDelete = myList.head.next.next.next.next
    myList.delete_link(linkToDelete.data)
    print(f"Test 07a: delete_link({linkToDelete}) => {myList}")
    myList.delete_link(12_000)
    print(f"Test 07b: delete_link(12_000) => {myList}\n")

    # Test method copy_list()
    newList = myList.copy_list()
    print(f"Test 08: copy_list() =>\nCopying list A:\n{myList}\nto list B:\n{newList}\n")

    # Test method reverse_list()
    print(f"Test 09: reverse_list() =>\n{myList.reverse_list()}\n")

    # Test method sort_list()
    randomList = LinkedList()
    [randomList.insert_last(random.randint(-i, i)) for i in range(myList.length)]
    print(f"Test 10: sort_list() =>\n{randomList.sort_list()}\n")

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    [randomList.insert_last(random.randint(-i, i)) for i in range(myList.length)]
    print(f"Test 11a: is_sorted({myList}) => {myList.is_sorted()}")
    print(f"Test 11b: is_sorted({randomList}) => {randomList.is_sorted()}\n")

    # Test method is_empty()
    emptyList = LinkedList()
    emptyList.delete_link(12)
    print(f"Test 12a: is_empty({emptyList}) => {emptyList.is_empty()}")
    print(f"Test 12b: is_empty({randomList}) => {randomList.is_empty()}\n")

    # Test method merge_list()
    secondList = randomList.sort_list()
    print(f"Test 13: merge_list(\n{myList}\nand\n{secondList}\n) =>\n{myList.merge_list(secondList)}\n")

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(f"Test 14a: is_equal(\n{myList}\nand\n{myList}) => {myList.is_equal(myList)}")
    print(f"Test 14b: is_equal(\n{myList}\nand\n{randomList}) => {myList.is_equal(randomList)}\n")

    # Test remove_duplicates()
    duplicatesList = LinkedList()
    for i in range(25):
        randNum = random.randint(-i, i)
        if(random.randint(0, 1) == 0):
            for i in range(random.randint(0, i)):
                duplicatesList.insert_in_order(randNum)
        else:
            duplicatesList.insert_in_order(randNum)
    print(f"Test 15: remove_duplicates(\n{duplicatesList}\n) => {duplicatesList.remove_duplicates()}")

if __name__ == "__main__":
    main()