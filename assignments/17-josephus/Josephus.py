#  File: Josephus.py

#  Description: Assignment 17 | Josephus Problem (Circularly Linked List)

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 10-30-2019

#  Date Last Modified: 10-30-2019

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
        current = self.head
        newList = CircularList()
        newList.head = current
        while(current != self.tail):
            newList.insert(current.data)
            current = current.next
            if(current == self.tail):
                newList.tail = current
                newList.insert(current.data)
                break
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
        self.length -= 1
        if(self.head == None):
            return(None)
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
        self.length -= 1
        if(self.head == None):
            return(None)
        prev = start
        current = prev.next
        while(n - 1 > 1):
            prev = current
            current = current.next
            n -= 1
        prev.next = current.next
        if(current == self.head):
            self.head = prev.next
            self.tail.next = self.head
        if(current == self.tail):
            self.tail = prev
        return(prev.next.data)

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
    myFile = open(r"c:/users/matt/documents/school/2019/fall/cs-313e/assignments/17-josephus/josephus.txt", "r")
    data = [
        int(myFile.readline().strip()),
        int(myFile.readline().strip()),
        int(myFile.readline().strip())
    ]
    return(data)

def main():
    # extract data from input file
    data = get_data()
    [print(row) for row in data] 
    print()

    # create linked list of people of length data[0] (amount of people)
    people = CircularList()
    [people.insert(i + 1) for i in range(0, data[0], data[1])]
    print(people, "\n")

    # # reduce list to single person 
    # person = data[2]
    # while(people.length != 1):
    #     person = people.delete_after(people.find(person), data[2])
    #     print(person)
    # print()

    # using for manipulation
    m_people = people.copy()
    print(m_people)

    # finding certain people
    print(f"find(1) => {people.find(1)}")
    print(f"find({data[0] // 2}) => {people.find(data[0] // 2)}")
    print(f"find({data[0]}) => {people.find(data[0])}\n")

    # deleting certain people
    print(f"delete({people.delete(1)}) {people}")
    print(f"delete({people.delete(7)}) {people}")
    print(f"delete({people.delete(data[0])}) {people}\n")

    # deleting after certain people
    print(f"{people.delete_after(people.find(1), 3)} => {people}\n")
    print(f"{people.delete_after(people.find(20), 3)} => {people}\n")
    print(f"{people.delete_after(people.find(39), 3)} => {people}\n")

main()
