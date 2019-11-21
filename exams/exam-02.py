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
        str_connect = ", "
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
            self.head.prev = None
            if(current == self.tail):
                self.tail = None
        elif(current == self.tail):
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev = current.prev
            current.next.prev = prev
            prev.next = current.next
        return(current)

# Q2:
# Create a hash table that uses a separate chaining to hash and store names.
# Separate chaining is using a LinkedList at each index as a means to avoid linear probing.
# Use a singly LinkedList to create the buckets for each index in the hash table.
# Assume that there is a hash function that returns an index to your table.
#
# Write the create_hash_table function that creates a list where each elements is
# None to start with. Assume that the Link class has already been written for you.
# Write the insert_name function that adds a string to the hash table and a 
# find_name function to find a name in the table. The hash table must be a list
# of Links.
class Link(object):
    # link constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    # handle str representation
    def __str__(self):
        return(f"{self.data}")

def get_hash(name, size):
    # assume that this function will apply a hash function to a 
    # name and give you an index for where to place your string
    # in a list of length size
    hash_idx = 0
    name = name.lower()
    for i in range(len(name)):
        letter = ord(name[i]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return(hash_idx)

# initialize and return a hash table filled with None
def create_hash_table(size):
    return([None for i in range(size)])

# insert a name into the table, do not return anything
def insert_name(h_table, name):
    h_size = len(h_table)
    h_index = get_hash(name, h_size)
    if(h_table[h_index] == None):
        h_table[h_index] = Link(name)
    else:
        current = h_table[h_index]
        while(current.next != None):
            current = current.next
        current.next = Link(name)

# find a name in the table, return True if name is there and False otherwise
def find_name(h_table, name):
    h_size = len(h_table)
    h_index = get_hash(name, h_size)
    if(h_table[h_index] == None):
        return(False)
    current = h_table[h_index]
    while(current != None):
        if(current.data == name):
            return(True)
        current = current.next
    return(False)

# print the hash table to format for linked lists
def print_hash_table(h_table):
    total_str = ""
    for i in range(len(h_table)):
        row_str = f"{i}: "
        if(h_table[i] != None):
            current = h_table[i]
            str_connect = ", "
            while(current != None):
                row_str += f"{current}{str_connect}"
                current = current.next
            row_str = row_str[:-len(str_connect)]
        else:
            row_str += "None"
        total_str += row_str + "\n"
    print(total_str[:-1])

# Q3:
# Write a function is_balanced that takes as input a string that contains
# among other characters parentheses, square brackets, curly braces, and chevron
# brackets. It returns True if these are properly nested and False otherwise. We say a bracket
# is properly nested if it is closed and before the brackets it is in are closed.
# For instance, ([]) is properly nested, but ([)] is not. The function will
# return True for an empty string or a string that has no brackets. You must use
# a Stack. Assume that the Stack ckass hass been written for you. Here are the brackets
# that you should consider.
#
# is_balanced("abcdef") => True
# is_balanced("(a + b) * [d * f]") => True 
# is_balanced("(a + $) b = ) (a ( )") => False
# is_balanced("())") => False
# is_balanced("([{]})") => False 
# is_balanced("[n] > [m]") => False
# is_balanced("") => True
class Stack(object):
    # stack constructor (built with Python list)
    def __init__(self):
        self.stack = []
    
    # push a value to the stack
    def push(self, value): 
        self.stack.append(value)

    # pop an elemnet from the stack
    def pop(self):
        if(len(self.stack) > 0):
            return(self.stack.pop())
        return(None)

    # peek at the element at the top of the stack
    def peek(self):
        if(len(self.stack) > 0):
            return(self.stack[-1])
        return(None)

def is_balanced(string):
    stack = Stack()
    for char in string:
        if(char == "(" or char == "[" or char == "{" or char == "<"):
            stack.push(char)
        elif(char == ")" or char == "]" or char == "}" or char == ">"):
            if (char == ")" and stack.peek() == "(") or (char == "]" and stack.peek() == "[") or (char == "}" and stack.peek() == "{") or (char == ">" and stack.peek() == "<"):
                stack.pop()
            else:
                return(False)
    return(len(stack.stack) == 0)

# Q4:
# Assume that there is the Stack object. You are given the sequence of distinct
# elements that are pushed as a list. You are also given the series of pops of 
# those elements as a list. Write a function is_valid that returns True if the 
# list of pops can be obtained from some combination of pushes and pops.
#
# For example if the push_list = [1, 2, 3, 4] and the pop_lists = [2, 4, 3, 1], 
# then your function will return True. Here is the combination - push(1), push(2),
# pop(2), push(3), push(4), pop(4), pop(3), pop(1).
def is_valid(push_list, pop_list):
    stack = Stack()
    for num in push_list:
        stack.push(num)
        while(len(stack.stack) > 0 and stack.peek() == pop_list[0]):
            stack.pop()
            if(len(pop_list) == 1):
                break
            pop_list = pop_list[1:]
    return(len(stack.stack) == 0)

# Q5:
# A chef has cooked a stack of pancakes, but the pancakes are all different sizes.
# He would like to order them such that the largest pancake is at the bottom
# and the smallest pancake is on the top. He has a spatula that he can insert 
# anywhere in the stack of pancakes and flip the pancakes on top of the spatula.
# Devise and code and algorithm that will sort the pancakes in ascending order
# with the minimum number of flips. The input parameter, sizes, is an list of
# diameters of the initial stack of pancakes. Given sizes = [7, 2, 5, 3, 4, 6].
# 
# Only the following operations are allowed:
# Get a slice of the array: slice = sizes[2:5] => [5, 3, 4]
# Reverse the slice: slice.reverse() => [4, 3, 5]
# Get the maximum in the slice: max(slice) => 5 
# Find the index of the maximum element: sizes.index(5) => 2
# Add slices together with either extend() or the + operator
def pancake_sort(sizes):
    if(len(sizes) == 1):
        return(sizes)
    else:
        flapjack = max(sizes)
        flip_stack = sizes[:sizes.index(flapjack) + 1]
        print(flip_stack)

# EC:

def main():
    # Q1 - Doubly Linked List
    print(f"Q1: Doubly Linked List Implementation")
    size = 10
    myList = DoublyLinkedList()
    [myList.insert_in_order(random.randint(-size, size)) for i in range(size)]
    print(myList)
    [print(f"myList.delete({i + 1}) => {myList.delete(i + 1)}") for i in range(size)]
    print(myList, "\n")

    # Q2 - Hash table w/ Linked List collision handling
    print(f"Q2: Hash Table w/ Linked List Collision Handling")
    h_table = create_hash_table(5)
    names = ["Cooper", "Matt", "Zoe", "Peter", "Jonathan", "MJ"]
    [insert_name(h_table, name) for name in names]
    print_hash_table(h_table)
    name = "Cooper"
    print(f"find_name(h_table, '{name}') => {find_name(h_table, name)}")
    print(f"find_name(h_table, 'Phyllis') => {find_name(h_table, 'Phyllis')}")
    name = "Peter"
    print(f"find_name(h_table, '{name}') => {find_name(h_table, name)}\n")

    # Q3 - Expression Balancing w/ Stacks
    print(f"Q3: Expression Balancing w/ Stacks")
    test_string = "(a + b) * [d * f]"
    print(f"is_balanced('{test_string}') => {is_balanced(test_string)}")
    test_string = "(a + $) b = ) (a ( )"
    print(f"is_balanced('{test_string}') => {is_balanced(test_string)}")
    test_string = ""
    print(f"is_balanced('{test_string}') => {is_balanced(test_string)}")
    test_string = "[n] > [m]"
    print(f"is_balanced('{test_string}') => {is_balanced(test_string)}")
    test_string = "([{]})"
    print(f"is_balanced('{test_string}') => {is_balanced(test_string)}\n")

    # Q4 - Valid Stack Push / Pop Sequence
    print(f"Q4: Valid Stack Push / Pop Sequences")
    push_list = [1, 2, 3, 4]
    pop_list = [2, 4, 3, 1]
    print(f"is_valid({push_list}, {pop_list}) => {is_valid(push_list, pop_list)}")
    pop_list = [4, 3, 1, 2]
    print(f"is_valid({push_list}, {pop_list}) => {is_valid(push_list, pop_list)}")

    # Q5 - Pancake Sorting
    print(f"Q5: Pancake Sort")
    pancakes = [7, 2, 5, 3, 4, 6]
    print(f"pancake_sort({pancakes}) => {pancake_sort(pancakes)}")

main()