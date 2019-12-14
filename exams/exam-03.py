# dependendies
import random
import math

# Stack
class Stack(object):
    # constructor
    def __init__(self):
        self.stack = []

    # returns and DOES NOT remove topmost element
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    # returns and removes topmost element
    def pop(self):
        return self.stack.pop()

    # add an element to the top of the stack
    def push(self, data):
        self.stack.append(data)

# Node (for binary (search) trees)
class Node(object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # handle str representation
    def __str__(self):
        return str(self.data)

    # returns True if node has at least one child, False otherwise
    def has_child(self):
        return self.left != None or self.right != None

# Tree class
class Tree(object):
    # constructor
    def __init__(self):
        self.root = None
    
    # prints out all nodes at the given level
    def print_level (self, level):
        if(level < 1):
            return
        def print_level_helper(level, node):
            if(node != None):
                if(level == 1):
                    print(f"{node}", end=" ")
                else:
                    print_level_helper(level - 1, node.left)
                    print_level_helper(level - 1, node.right)
        print_level_helper(level, self.root)

    # insert data into the tree
    def insert (self, data):
        new_node = Node (data)
        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.left
                else:
                    current = current.right
            if (data < parent.data):
                parent.left = new_node
            else:
                parent.right = new_node

    # Returns the height of the tree
    def get_height (self):
        if self.root == None:
            return -1
        def get_height_helper(node, height):
            if node != None:
                if not node.has_child():
                    return height
                else:
                    if node.left != None and node.right != None:
                        return max(get_height_helper(node.left, height + 1), get_height_helper(node.right, height + 1))
                    elif node.left != None:
                        return get_height_helper(node.left, height + 1)
                    else:
                        return get_height_helper(node.right, height + 1)
            return 0
        return get_height_helper(self.root, 0)

    # ==========================
    # ====== QUESTION 01 =======
    # ==========================
    def is_perfect(self):
        max_height = self.get_height()
        def is_perfect_helper(node, current_height):
            # node has no children
            if node.left == node.right == None:
                if current_height == max_height:
                    return True
                return False
            # node only has left child
            elif node.left != None and node.right == None:
                return False
            # node only has right child
            elif node.left == None and node.right != None:
                return False
            # node has both children so return True if both children are also perfect
            else:
                current_height += 1
                return is_perfect_helper(node.left, current_height) and is_perfect_helper(node.right, current_height)
        if self.root != None:
            return is_perfect_helper(self.root, 0)
        return False

    # ==========================
    # ====== QUESTION 04 =======
    # ==========================
    def inorder(self):
        if(self.root != None):
            stack = Stack()
            h_table = {} # stores already-printed nodes
            current = self.root
            stack.push(current)
            while(stack.peek() != None):
                if current.left != None and current.left not in h_table:
                    stack.push(current.left)
                else:
                    print(current)
                    h_table[stack.pop()] = True
                    if current.right != None:
                        stack.push(current.right)
                current = stack.peek()

# Vertex class
class Vertex(object):
    # constructor
    def __init__(self, label):
        self.label = label
        self.visited = False

# Graph class
class Graph(object):
    # constructor
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []
        self.adj_list = []

    # ==========================
    # ====== QUESTION 03 =======
    # ==========================
    # returns index of the given vertex label
    def get_index(self, label):
        for i in range(len(self.vertices)):
            if label == self.vertices[i].label:
                return i
        return -1
    
    # returns list of immediate neighbors (empty if none exist) given a vertex label
    def get_neighbors(self, label):
        neighbors = []
        vertex_index = self.get_index(label)
        for i in range(len(self.adj_matrix[vertex_index])):
            if self.adj_matrix[vertex_index][i] > 0:
                neighbors.append(self.vertices[i])
        return neighbors

    # prints vertices within distance k vertices from x
    def print_within(self, x, k):
        if k == 0:
            print(x)
        else:
            print(x)
            neighbors = self.get_neighbors(x.label)
            for neighbor in neighbors:
                self.print_within(neighbor, k - 1)

    # ==========================
    # ====== QUESTION 05 =======
    # ==========================
    def add_vertex(self, label):
        self.vertices.append(Vertex(label))

    def add_directed_edge(self, start, finish, weight=1):
        start_idx = self.get_index(start.label)
        self.adj_list[start_idx].update(finish, weight)
    
    def add_undirected_edge(self, start, finish, weight=1):
        start_idx = self.get_index(start.label)
        self.adj_list[start_idx].update(finish, weight)
        finish_idx = self.get_index(finish.label)
        self.adj_list[finish_idx].update(start, weight)
    
    def get_adj_unvisited_vertex(self, vertex):
        vertex_idx = self.get_index(vertex.label)
        for key_vertex in self.adj_list[vertex_idx].keys():
            if key_vertex.visited == False:
                key_vertex.visited = True
                return key_vertex 
        return None  

# Do any TWO questions from Q1 to Q5, any ONE question from Q6 to
# Q8, and you must do Q9. Unless otherwise indicated, you may
# define and use helper functions. Do not add additional
# arguments to the functions you are asked to define.

# Q1: 
# A perfect binary tree is a binary tree in which all
# interior nodes have two children and all leaves have the same
# depth or same level. Given a binary tree, write a method to
# determine if it is perfect. Return True if it is perfect, and
# false if not. The Node and Tree class have been defined below.
# You may write a helper method if you wish. 
# ANSWER: Refer to lines 98-121

# Q2:
# Given a sorted list of integers, write a method to create a
# balanced binary search tree. The list contains the proper
# number of elements to create a balanced tree. Hint: write a
# helper method that locates the median of the list.
def create_BST(nums):
    result_tree = Tree()
    def create_BST_helper(nums):
        if len(nums) == 1:
            result_tree.insert(nums[0])
        else:
            mid = len(nums) // 2
            result_tree.insert(nums[mid])
            create_BST_helper(nums[:mid])
            create_BST_helper(nums[mid + 1:])
    if len(nums) > 0:
        create_BST_helper(nums)
    return result_tree

# Q3: 
# Given an undirected graph and a starting vertex x, print
# all the vertex labels within a distance k (k is the number
# of vertices you need to go through to get to your destination)
# from the starting vertex. The Graph and Vertex classes are
# defined below. You may only utilize methods defined below (no
# helper methods!)
# ANSWER: Refer to lines 157-184

# Q4: 
# Given a binary search tree, write a method to print an inorder
# traversal without recursion. Use a stack to help you achieve
# this. Assume the stack class has already been written for you
# - you may use the Stack classes push(), pop(), and peek()
# methods. The method header is as follows:
# ANSWER: Refer to lines 123-140

# Q5:
# Implement the Graph class using only an adjacency list, not
# an adjacency matrix. This adjacency list shall be a list of
# dictionaries. The first dictionary refers to edges starting
# from the first vertex and so on. The key for each key-value
# pair within a dictionary is the ending vertex, and the value
# is the weight of this edge.
# ANSWER: Refer to lines 186-208

# Q6:
# A: Using the given graph, following Kruskal's algorithm, list
# the edges in the order that they would be added that would
# result in the minimum spanning tree for this graph.
# B: Do the same thing but with Prim's algorithm starting at the
# vertex C (represent the edges as a pair of vertices (v1, v2)).

# Q7:
# Add the list below to an empty AVL tree. Balance as you add.
# [3, 9, 4, 5, 32, 29, 16, 31, 1, 77, 7]
# A: What would the tree look like when you add 5?
# B: What would the tree look like when you add all the elements 
# of the list?
# C: Why do we use self-balancing trees, what are the benefits?

# Q8:
# Add the list below to an empty max heap.
# [3, 9, 4, 5, 32, 29, 16, 31, 1, 77, 7]
# A: What would the heap look like when you add 5?
# B: What would the heap look like when you add all the elements 
# of the list?
# C: Why do we use max heaps, what are the benefits? 

# Q9:
# Using Dijkstra's shortest path algorithm, find the shortest
# paths from vertex D to all other vertices in the above graph.

# EC:
# You have a set of bottles with different volumes filled with
# your favorite drink. You may drink as much as you want with
# the constraint that you cannot drink from 2 adjacent bottles.
# How can you maximize your intake? Fill the table with columns
# for the index, volume, and s(v) which is the largest sum so far. 

# wrapper method for tree level printing (avoid writing loop every time)
def print_tree_wrapper(tree):
    for i in range(1, tree.get_height() + 2):
        print(f"L{i}:", end=" ")
        tree.print_level(i)
        print()

def main():
    print(f"Q1: Test for perfect binary trees\n")
    size = 31
    tree = Tree()
    print_tree_wrapper(tree)
    print(f"is_perfect() => {tree.is_perfect()} (False)\n")
    tree.insert(random.randint(0, size * 100))
    print_tree_wrapper(tree)
    print(f"is_perfect() => {tree.is_perfect()} (True)\n")
    tree.insert(tree.root.data - tree.root.data)
    print_tree_wrapper(tree)
    print(f"is_perfect() => {tree.is_perfect()} (False)\n")
    tree.insert(tree.root.data + tree.root.data)
    print_tree_wrapper(tree)
    print(f"is_perfect() => {tree.is_perfect()} (True)\n")
    exp = 6
    nums = [i + 1 for i in range((2 ** exp) - 1)]
    tree = create_BST(nums)
    print_tree_wrapper(tree)
    print(f"is_perfect() => {tree.is_perfect()} (True)\n")

    print(f"Q2: Creating BSTs from sorted list of numbers\n")
    nums = [i * i for i in range((2 ** exp) - 1)]
    print(f"create_BST([]) => {create_BST([]).root}\n")
    tree = create_BST([50])
    print(f"create_BST([50]) => {tree.root}")
    print(f"is_perfect() => {tree.is_perfect()} (True)\n")
    print(f"create_BST(\n{nums}\n) =>")
    tree = create_BST(nums)
    print_tree_wrapper(tree)
    print(f"is_perfect() => {tree.is_perfect()} (True)\n")

main()