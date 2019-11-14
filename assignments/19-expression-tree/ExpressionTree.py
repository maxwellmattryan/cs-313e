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
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.tol = 10e-8

    # handle str representation
    def __str__(self):
        if(isinstance(self.data, float)):
            if(self.data % 1 <= self.tol):
                return(f"{self.data:.0f}")
        return(f"{self.data}")
    
    # print the tree
    def print(self, levels=None):
        if levels==None:
            levels=[self]
        nextLevel=[]
        for node in levels:
            if(node == None):
                print(" ", end=" ")
            else:
                print(node.data, end=" ")
        for node in levels:
            if(node != None):
                nextLevel.extend([node.left, node.right])
        print()
        if nextLevel:
            node.print(nextLevel) 

# Tree class (implemented with Nodes)
class Tree (object):
    # tree constructor
    def __init__ (self):
        self.root = Node(None)
        self.operators = ["+", "-", "*", "/", "//", "%", "**"]

    def create_tree (self, expr_list):
        current = self.root
        expr_stack = Stack()
        for exp_token in expr_list:
            if exp_token == "(":
                current.left = Node(None)
                expr_stack.push(current)
                current = current.left
            elif exp_token in self.operators:
                current.data = exp_token
                current.right = Node(None)
                expr_stack.push(current)
                current = current.right
            elif exp_token == ")":
                if expr_stack.size() > 0:
                    current = expr_stack.pop()
            else:
                current.data = float(exp_token)
                current = expr_stack.pop()

    def evaluate(self, aNode):
        if aNode.data in self.operators:
            result = self.operate(self.evaluate(aNode.left), self.evaluate(aNode.right), aNode.data)
            return result
        return aNode.data

    # return result of mathematical operation
    def operate(self, operand1, operand2, operator):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        elif operator == "//":
            return operand1 // operand2
        elif operator == "%":
            return operand1 % operand2
        elif operator == "**":
            return operand1 ** operand2

    def pre_order (self, aNode):
        if(aNode != None):
            print(aNode, end= " ")
            self.pre_order(aNode.left)
            self.pre_order(aNode.right)

    # print the tree
    def print(self, levels=None):
        if(self.root != None):
            self.root.print()

    def post_order (self, aNode):
        if(aNode != None):
            self.post_order(aNode.left)
            self.post_order(aNode.right)
            print(aNode, end=" ")

# read in string expression from file
def get_expr():
    my_file = open("./expression.txt", "r")
    return my_file.readline().split(" ")

def main():
    expr = get_expr()
    myTree = Tree()
    myTree.create_tree(expr)
    print(f"{' '.join(expr)} = {myTree.evaluate(myTree.root)}\n")

    print("Prefix Expression:", end=" ")
    myTree.pre_order(myTree.root)
    print("\n")

    print("Postfix Expression:", end=" ")
    myTree.post_order(myTree.root)

main()