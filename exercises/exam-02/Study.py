import random

# Q5 - Stack / Queue implementation via (singly) linked lists
# Queue - enqueue, dequeue, isEmpty, size
class Link(object):
    # link constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    # str representation of link
    def __str__(self):
        return(f"{self.data}")

# Stack - push, pop, peek, isEmpty, size
class Stack(object):
    # stack constructor
    def __init__(self):
        self.head = self.tail = None
        self.length = 0 

    # str representation
    def __str__(self):
        if(self.head == None):
            return("")
        current = self.head
        while(current.next != None):
            print(current, end=", ")
            current = current.next
        return(str(current))

    # return the topmost element on stack
    def peek(self):
        return(self.tail)

    # popping from the stack
    def pop(self):
        if(self.head == None):
            return(None)
        self.length -= 1
        prev = current = self.head
        while(current != self.tail):
            prev = current
            current = current.next
        if(current == self.head):
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev
        return(current)

    # pushing to the stack
    def push(self, data):
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new

def main():
    print(f"Q1: Given a list of words, find the largest set of words that are anagrams")
    print(f"Q2: Use a stack implementation to find a palindrome")
    print(f"Q3: Convert between prefix, infix, and postfix notation")
    print(f"Q4: Return if a given html file is valid (considering its tags)")
    
    # Q5
    print(f"Q5: Use a linked list to represent stacks or queues and write their respective methods")
    # stack implementation
    myStack = Stack() # create stack
    [myStack.push(i + 1) for i in range(20)] # push values in order
    print(f"{myStack}\npeek() => {myStack.peek()}") # peek and print result
    [print(myStack.pop()) for i in range(myStack.length + 1)] # pop each element off the list
    print(f"{myStack}\nHead = {myStack.head}, Tail = {myStack.tail}") # print empty stack 

    # queue implementation

    print(f"Q6: Implement a doubly-linked list class")
    print(f"Q7: Pancake chef problem")
    print(f"Q8: Radix sort (using queue implementation)")

main()