import random

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

# Q7 - Pancake flipping problem
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

    # # Q3
    # print(f"Q3: Convert between prefix, infix, and postfix notation")
    
    # # Q4
    # print(f"Q4: Return if a given html file is valid (considering its tags)")
    
    # # Q5
    # print(f"Q5: Use a linked list to represent stacks or queues and write their respective methods")
    # # stack implementation
    # myStack = Stack() # create stack
    # [myStack.push(i + 1) for i in range(20)] # push values in order
    # print(f"{myStack}\npeek() => {myStack.peek()}") # peek and print result
    # [print(myStack.pop()) for i in range(myStack.length + 1)] # pop each element off the list
    # print(f"{myStack}\nHead = {myStack.head}, Tail = {myStack.tail}") # print empty stack 

    # # queue implementation

    # # Q6
    # print(f"Q6: Implement a doubly-linked list class")
    
    # Q7
    print(f"Q7: Pancake chef problem")
    pancakes = [random.randint(1, i * 10) for i in range(1, 20)]
    print(pancakes)
    pancakes = flip(pancakes)
    print(pancakes)
    
    # # Q8
    # print(f"Q8: Radix sort (using queue implementation)")

main()