#  File: Josephus.py

#  Description: Assignment 17 | Josephus Problem (Circularly Linked List)

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 10-30-2019

#  Date Last Modified: 11-04-2019

class Link(object):
    # Link constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # overload string method
    def __str__(self):
        return(f"{self.data}")

class CircularList(object):
    # Constructor
    def __init__ (self): 
        self.head = self.tail = None
        self.length = 0

    # Insert an element (value) in the list
    def insert (self, data):
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            new.next = self.head
            self.tail.next = new
            self.tail = new

    # Copy the list and return it
    def copy(self):
        if(self.head == None):
            return(None)
        newList = CircularList()
        current = self.head
        while(current != self.tail):
            newList.insert(current.data)
            current = current.next
        newList.insert(current.data)
        return(newList)

    # Find the link with the given data (value)
    def find (self, data):
        if(self.head == None):
            return(None)
        current = self.head
        while(current.data != data):
            if(current == self.tail):
                return(None)
            current = current.next
        return(current)

    # Delete a link with a given data (value)
    def delete (self, data):
        if(self.head == None):
            return(None)
        self.length -= 1
        prev = current = self.head
        while(current.data != data):
            if(current == self.tail):
                return(None)
            prev = current
            current = current.next
        prev.next = current.next
        if(current == self.head):
            self.head = prev.next
            self.tail.next = self.head
        if(current == self.tail):
            self.tail = prev
        return(current)

    # Delete the nth link starting from the Link start 
    # Return the next link from the deleted Link
    def delete_after (self, start, n):
        if(self.head == None):
            return(None)
        self.length -= 1
        prev = current = start
        while(n - 1 > 0):
            prev = current
            current = current.next
            n -= 1
        prev.next = current.next
        if(current == self.head):
            self.head = prev.next
        elif(current == self.tail):
            self.tail = prev
        print(current)
        return(current.next)

    # Return a string representation of a Circular List
    def __str__ (self):
        if(self.head == None):
            return("")
        current = prev = self.head
        listItems = []
        while(prev != self.tail):
            if(current == self.head):
                listItems.append("<::" + str(current.data))
            elif(current == self.tail):
                listItems.append(str(current.data) + "::>")
            else:
                listItems.append(str(current.data))
            prev = current
            current = current.next
        return(' '.join(listItems))

# returns data from input file (num of people, ordering of men, beginning count position)
def get_data():
    myFile = open("josephus.txt", "r")
    data = [
        int(myFile.readline().strip()),
        int(myFile.readline().strip()),
        int(myFile.readline().strip())
    ]
    return(data)

def main():
    # extract data from input file
    data = get_data()

    # create linked list of people of length data[0] (amount of people)
    people = CircularList()
    [people.insert(i + 1) for i in range(0, data[0])]

    # reduce list to single person 
    last_person = people.find(data[1])
    while(people.length > 0):
        last_person = people.delete_after(people.find(last_person.data), data[2])

main()
