import random
import time

# Q1 - Given a word list as a dictionary, find the largest set of words
# that are anagrams. Anagrams are words such that rearranging the characters
# of one equals the other (i.e. "stop", "pots" = anagrams)
# goes through input file and returns the word list
def get_word_list():
    myFile = open("resources/words.txt", "r")
    words = {line.strip() : 1 for line in myFile}
    myFile.close()
    return(words)
def permute(a, lo, hi, words, h_memo, word_set):
    if(lo == hi):
        string = ''.join(a)
        if(string in words):
            word_set.add(string)
            h_memo[string] = 1
    else:
        for i in range(lo, hi):
            a[i], a[lo] = a[lo], a[i]
            permute(a, lo + 1, hi, words, h_memo, word_set)
            a[i], a[lo] = a[lo], a[i]

# Q2 - Implement a stack to evaluate if a string is a palindrome or not
def is_palindrome(string):
    # if string is odd length, then remove irrelevant middle letter
    if(len(string) % 2 == 1):
        string = string[:len(string) // 2] + string[len(string) // 2 + 1:]
    stack = []
    for i in range(len(string)):
        if(len(stack) == 0 or stack[-1] != string[i]):
            stack.append(string[i])
        else:
            stack.pop()
    return(len(stack) == 0)

# Q3 - Given an array of tokens, evaluate it accordingly 
def operate(operand1, operand2, operator):
    if(operator == "+"):
        return(operand1 + operand2)
    elif(operator == "-"):
        return(operand1 - operand2)
    elif(operator == "*"):
        return(operand1 * operand2)
    elif(operator == "/"):
        return(operand1 / operand2)
    elif(operator == "//"):
        return(operand1 // operand2)
    elif(operator == "%"):
        return(operand1 % operand2)
    elif(operator == "**"):
        return(operand1 ** operand2)
def postfix_eval(tokens):
    stack = []
    n = 0
    while(n < len(tokens)):
        if(isinstance(tokens[n], int)):
            stack.append(tokens[n])
        else:
            operator = tokens[n]
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = operate(operand1, operand2, operator)
            stack.append(result)
        n += 1
    return(stack[0])
def prefix_eval(tokens):
    stack = []
    n = 1
    while(n <= len(tokens)):
        if(isinstance(tokens[-n], int)):
            stack.append(tokens[-n])
        else:
            operator = tokens[-n]
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = operate(operand1, operand2, operator)
            stack.append(result)
        n += 1
    return(stack[0])

# Q5 - Stack / Queue implementation via (singly) linked lists
# Queue - enqueue, dequeue, is_empty, size
class Link(object):
    # link constructor
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    # str representation of link
    def __str__(self):
        return(f"{self.data}")
# Stack - push, pop, peek, is_empty, size
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

    # returns True if stack is empty
    def is_empty(self):
        return(self.length == 0)

    # return size of stack
    def size(self):
        return(self.length)

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
# Queue - enqueue, dequeue, isEmpty, size
class Queue(object):
    # queue constructor
    def __init__(self):
        self.first = self.last = None
        self.length = 0
    
    # handle str representation
    def __str__(self):
        if(self.first == None):
            return("")
        current = self.first
        while(current.next != None):
            print(current, end=", ")
            current = current.next
        return(str(current))

    # returns True if stack is empty
    def is_empty(self):
        return(self.length == 0)    

    # dequeue returns the next element and removes from queue
    def dequeue(self):
        if(self.first == None):
            return(None)
        self.length -= 1
        item = self.first
        if(item.next == None):
            self.first = self.last = None
        else:
            self.first = item.next
        return(item)
            
    
    # queue places an element into the last position
    def enqueue(self, data):
        self.length += 1
        new = Link(data)
        if(self.first == None):
            self.first = new
        else:
            self.last.next = new
        self.last = new

    # return size of stack
    def size(self):
        return(self.length)

# Q5 - Implement a doubly-linked list with the methods:
# prepend, append, insert, remove, sort, reverse, find
class DoublyLinkedList(object):
    # doubly linked list constructor
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    # handles str representation
    def __str__(self):
        if(self.head == None):
            return("")
        end_str = ", "
        string = ""
        current = self.head
        while(current != None):
            string += str(current) + end_str
            current = current.next
        return(string[:len(string) -  len(end_str)])

    # append an item to the tail of the list
    def append(self, data):
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    # insert an item (data) after the given existing node (target)
    def insert(self, data, target):
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        elif(target == self.tail):
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            new.next = target.next
            new.next.prev = new
            new.prev = target
            target.next = new

    # insert an item(data) in order in a list
    def insert_in_order(self, data):
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            prev = current = self.head
            while(data >= current.data):
                prev = current
                current = current.next
                if(current == None):
                    new.prev = prev
                    prev.next = new
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

    # return if list is empty
    def is_empty(self):
        return(self.length == 0)

    # given a data value, return first occurence of that value or None otherwise
    def find(self, target_data):
        if(self.head == None):
            return(None)
        current = self.head
        while(current.data != target_data):
            current = current.next
            if(current == None):
                return(None)
        return(current)

    # prepend an item to the head of the list
    def prepend(self, data):
        self.length += 1
        new = Link(data)
        if(self.head == None):
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    # remove and return a target link from the list, return None if it isn't found
    def remove(self, target_data):
        if(self.head == None):
            return(None)
        self.length -= 1
        current = self.head
        while(current.data != target_data):
            current = current.next
            if(current == None):
                return(None)
        if(current == self.head):
            self.head = current.next
            self.head.prev = None
            if(current == self.tail):
                self.tail = None
        elif(current == self.tail):
            self.tail = current.prev
            self.tail.next = None
        else:
            prev = current.prev
            prev.next = current.next
            current.next.prev = prev
        return(current)

    # reverse and return new list
    def reverse(self):
        if(self.head == None):
            return(None)
        new = DoublyLinkedList()
        current = self.head
        while(current != None):
            new.prepend(current.data)
            current = current.next
        return(new)

    # sort and return new list
    def sort(self, reverse=False):
        if(self.head == None):
            return(None)
        new = DoublyLinkedList()
        current = self.head
        while(current != None):
            new.insert_in_order(current.data)
            current = current.next
        if(reverse):
            new = new.reverse()
        return(new)

# Q6 - Pancake flipping problem
def flip(pancakes):
    if(len(pancakes) == 1):
        return(pancakes)
    else:
        # find index of largest element
        l_index = pancakes.index(max(pancakes)) 
        # create sub list from largest pancake to top pancake
        s_list = pancakes[l_index:]
        # reverse so that largest pancake is on top
        s_list.reverse()
        # combine pancakes with pancakes that you flipped
        pancakes = pancakes[:l_index] + s_list
        # reverse so that the largest is on bottom-most position
        pancakes.reverse()
        # return list of pancakes[0] (largest element) and the rest of the pancakes flipped
        return([pancakes[0]] + flip(pancakes[1:]))

# Q7 - Radix sort (queue implementation)
def radix_sort(nums):
    number_place = 1
    while(True):
        number_queues = [[] for i in range(10)]
        for num in nums:
            s_num = str(num)
            if(number_place <= len(s_num)):
                number_queues[int(s_num[-number_place])].append(num)
            else:
                number_queues[0].append(num)
        if(len(number_queues[0]) == len(nums)):
            return(nums)
        nums = []
        for queue in number_queues:
            for num in queue:
                nums.append(num)
        number_place += 1

def main():
    # Q1
    print(f"Q1: Given a list of words, find the largest set of words that are anagrams")
    words = get_word_list()
    h_memo = {}
    anagram_sets = []
    for word in words.keys():
        if(word not in h_memo and len(word) < 6):
            word_set = set()
            permute(list(word), 0, len(word), words, h_memo, word_set)
            if(len(word_set) > 1):
                anagram_sets.append(word_set)
    anagram_sets.sort(key=len)
    print(anagram_sets[-1], "\n")

    # Q2
    print(f"Q2: Use a stack implementation to find a palindrome")
    print(f"\"radar\" => {is_palindrome('radar')}")    
    print(f"\"abbaabba\" => {is_palindrome('abbaabba')}")    
    print(f"\"false\" => {is_palindrome('false')}")    
    print(f"\"racecar\" => {is_palindrome('racecar')}\n")    

    # Q3
    print(f"Q3: Convert between prefix, infix, and postfix notation")
    t_prefix = ["*", 2, "+", "*", 2, 10, "+", 5, 3]
    print(f"prefix_eval({t_prefix}) => {prefix_eval(t_prefix)}")
    t_postfix = t_prefix
    t_postfix.reverse()
    print(f"postfix_eval({t_postfix}) => {postfix_eval(t_postfix)}\n")
    
    # Q4(A) stack implementation
    print(f"Q4(A): Implement a stack using a linked list")
    myStack = Stack() # create stack
    [myStack.push(i + 1) for i in range(20)] # push values in order
    print(f"{myStack}")
    print(f"peek() => {myStack.peek()}") # peek and print result
    [print(f"pop() => {myStack.pop()}") for i in range(myStack.length // 2)] # pop each element off the list
    print(f"{myStack}\nHead = {myStack.head}, Tail = {myStack.tail}, length = {myStack.length}, is_empty() => {myStack.is_empty()}\n") # print empty stack 
    
    # Q4 (B) queue implementation
    print(f"Q4(B): Implement a queue using a linked list")
    myQueue = Queue()
    [myQueue.enqueue(i + 1) for i in range(20)]
    print(f"{myQueue}")
    [print(f"dequeue() => {myQueue.dequeue()}") for i in range(myQueue.length // 2)]
    print(f"{myQueue}\nFirst = {myQueue.first}, Last = {myQueue.last}, length = {myQueue.length}, is_empty() => {myQueue.is_empty()}\n")

    # Q5
    print(f"Q5: Implement a doubly-linked list class")
    # prepending
    myList = DoublyLinkedList()
    [myList.prepend(i + 1) for i in range(10)]
    print(f"prepend(1-10) => {myList}")
    # appending
    myList = DoublyLinkedList()
    [myList.append(i + 1) for i in range(10)]
    print(f"append(1-10) => {myList}")
    # inserting (after)
    [myList.insert(i + 1, myList.find(i + 1)) for i in range(myList.length)]
    print(f"insert(1-10) => {myList}\nHead = {myList.head}, Tail = {myList.tail}, Length = {myList.length}, is_empty() => {myList.is_empty()}")
    # inserting data into list in sorted position
    [myList.insert_in_order(random.randint(1, myList.length)) for i in range(10)]
    print(f"insert_in_order(rand ints) => {myList}")
    # finding a node of a given value
    print(f"find(5) => {myList.find(5)}")
    # removing nodes from the linked list
    [myList.remove(i + 1) for i in range(myList.length // 2 // 2)]
    print(f"remove(1-5) => {myList}")
    # reverse the list and print
    myList = myList.reverse()
    print(f"reverse() => {myList}")
    # make random list to sort
    myList = DoublyLinkedList()
    [myList.append(random.randint(1, 20)) for i in range(20)]
    s_myList = myList.sort()
    print(f"sort({myList}) =>\n{s_myList}\n")

    # Q6
    print(f"Q6: Sort a stack of pancakes by only flipping")
    pancakes = [random.randint(1, 100) for i in range(1, 10)]
    print(f"flip({pancakes}) => {flip(pancakes)}\n")
    
    # Q7
    print(f"Q7: Radix sort (queue implementation)")
    myNums = [random.randint(1, 1_000_000) for i in range(1_000_000)]
    #print(f"radix_sort({myNums}) =>\n{radix_sort(myNums)}")
    totalTime = time.time()
    s_myNums = radix_sort(myNums)
    totalTime = time.time() - totalTime
    print(f"radix_sort([{myNums[0]}, ..., {myNums[len(myNums) - 1]}]) => [{s_myNums[0]}, ..., {s_myNums[len(s_myNums) - 1]}]")
    print(f"Total time = {totalTime:.03f}s")

main()