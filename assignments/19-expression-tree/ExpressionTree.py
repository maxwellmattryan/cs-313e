#  File: ExpressionTree.py

#  Description: Assignment 19 | Expression Tree

#  Student's Name: Matthew Maxwell

#  Student's UT EID: mrm5632

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 11-11-2019

#  Date Last Modified: 11-11-2019

# Stack class (implemented with ordinary list)
class Stack (object):
    # stack constructor
    def __init__(self, stack=[]):
        self.stack = stack

    # returns but doesn't delete topmost element on stack
    def peek(self):
        if(len(self.stack) > 0):
            return self.stack[-1]

    # return and delete topmost element on stack
    def pop(self):
        if(len(self.stack) > 0):
            return self.stack.pop()
    
    # push an element onto the stack
    def push(self, data):
        self.stack.append(data)

    # return size of stack instance
    def size(self):
        return len(self.stack)

# Node class
class Node (object):
    # node constructor
    def __init__(self, data, left=None, right=None, h_dist=0):
        self.data = data
        self.left = left
        self.right = right
        self.h_dist = h_dist
    
    # print the tree
    def print(self, levels=None):
        if levels==None:
            levels=[self]
        nextLevel=[]
        for node in levels:
            print(node.data, end=" ")
        for node in levels:
            nextLevel.extend([node.left, node.right])
        print('\n')
        if nextLevel:
            node.print(nextLevel) 

# Tree class (implemented with Nodes)
class Tree (object):
    # tree constructor
    def __init__ (self):
        self.root = Node(None)
        self.operators = ["+", "-", "*", "/", "//", "%", "**"]

    def create_tree (self, expr):
        current = self.root
        expr_stack = Stack()
        for exp_char in expr:
            if exp_char == "(":
                current.left = Node(None)
                expr_stack.push(current)
                current = current.left
            elif exp_char in self.operators:
                current.data = exp_char
                current.right = Node(None)
                expr_stack.push(current)
                current = current.right
            elif exp_char == ")":
                if expr_stack.size() > 0:
                    current = expr_stack.pop()
            else:
                current.data = int(exp_char)
                current = expr_stack.pop()

    def evaluate (self, aNode):
        ...
        
    def pre_order (self, aNode):
        ...

    # print the tree
    def print(self, levels=None):
        if(self.root != None):
            self.root.print()

    def post_order (self, aNode):
        ...

# read in string expression from file
def get_expr():
    my_file = open("./expression.txt", "r")
    return my_file.readline().replace(" ", "")

def main():
    myTree = Tree()
    myTree.create_tree(get_expr())
    myTree.print()

main()