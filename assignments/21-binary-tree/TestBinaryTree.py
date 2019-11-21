#  File: TestBinaryTree.py

#  Description: Assignment 21 | Binary Trees

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632  

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11-12-2019

#  Date Last Modified: 11-21-2019

import random

class Node (object):
    # node constructor
    def __init__(self, data):
        self.data = data
        self.left_child = self.right_child = None

    # handle str representation
    def __str__(self):
        return f"{self.data}"

    # return true if node has at least one child
    def has_child(self):
        return self.left_child != None or self.right_child != None

class Tree (object):
    # tree constructor
    def __init__(self):
        self.root = None

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
                    current = current.left_child
                else:
                    current = current.right_child
            if (data < parent.data):
                parent.left_child = new_node
            else:
                parent.right_child = new_node

    # Returns true if two binary trees are similar
    def is_similar (self, other):
        if(self.root == other.root == None):
            return True
        elif(self.root == None or other.root == None):
            return False
        else:
            def is_similar_helper(node_a, node_b):
                if(node_a == node_b == None):
                    return True
                elif(node_a.data == node_b.data):
                    return is_similar_helper(node_a.left_child, node_b.left_child) and is_similar_helper(node_a.right_child, node_b.right_child)
                else:
                    return False
            return is_similar_helper(self.root, other.root)

    # Prints out all nodes at the given level
    def print_level (self, level):
        def print_level_helper(level, node):
            if(node != None):
                if(level == 1):
                    print(f"{node}", end=" ")

                else:
                    print_level_helper(level - 1, node.left_child)
                    print_level_helper(level - 1, node.right_child)
        print_level_helper(level, self.root)

    # Returns the height of the tree
    def get_height (self):
        def get_height_helper(node, height):
            if(node != None):
                if(not node.has_child()):
                    return height
                else:
                    if(node.left_child != None and node.right_child != None):
                        return max(get_height_helper(node.left_child, height + 1), get_height_helper(node.right_child, height + 1))
                    elif(node.left_child != None):
                        return get_height_helper(node.left_child, height + 1)
                    else:
                        return get_height_helper(node.right_child, height + 1)
            return 0
        return get_height_helper(self.root, 0)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        def num_nodes_helper(node):
            if(node == None):
                return 0
            return 1 + num_nodes_helper(node.left_child) + num_nodes_helper(node.right_child)
        return num_nodes_helper(self.root)

def main():
    # Create three trees (two similar, one different)
    tree1 = Tree()
    tree2 = Tree()
    tree3 = Tree()

    # initialize tree size
    size = 250

    # insert same random element into tree1 and tree2 and different one into tree3 (which will *probably* cause a different height)
    for i in range(size):
        rand_num = random.randint(-size, size)
        tree1.insert(rand_num)
        tree2.insert(rand_num)
        tree3.insert(random.randint(-size, size))

    # Test your method is_similar()
    print(f"TEST: is_similar")
    print(f"tree1.is_similar(tree2) => {tree1.is_similar(tree2)}")
    print(f"tree1.is_similar(tree3) => {tree1.is_similar(tree3)}")
    print(f"tree1.is_similar(Tree()) => {tree1.is_similar(Tree())}")
    print(f"Tree().is_similar(tree1) => {Tree().is_similar(tree1)}")
    print(f"Tree().is_similar(Tree()) => {Tree().is_similar(Tree())}\n")

    # Print the various levels of two of the trees that are different
    print(f"TEST: print_level")
    print("Tree 1:")
    for i in range(1, tree1.get_height() + 2):
        print(f"L{i}:", end=" ")
        tree1.print_level(i)
        print()

    print("\nTree 2:")
    for i in range(1, tree2.get_height() + 2):
        print(f"L{i}:", end=" ")
        tree2.print_level(i)
        print()
    
    print("\nTree 3:")
    for i in range(1, tree3.get_height() + 2):
        print(f"L{i}:", end=" ")
        tree3.print_level(i)
        print()

    print("\nTree():")
    for i in range(1, Tree().get_height() + 2):
        print(f"L{i}:", end=" ")
        Tree().print_level(i)
        print()
    print()

    # Get the height of the two trees that are different
    print(f"TEST: get_height")
    print(f"tree1.get_height() => {tree1.get_height()}")
    print(f"tree2.get_height() => {tree2.get_height()}")
    print(f"tree3.get_height() => {tree3.get_height()}")
    print(f"Tree().get_height() => {Tree().get_height()}\n")

    # Get the total n
    print(f"TEST: num_nodes")
    print(f"tree1.num_nodes() => {tree1.num_nodes()}")
    print(f"tree2.num_nodes() => {tree2.num_nodes()}")
    print(f"tree3.num_nodes() => {tree3.num_nodes()}")
    print(f"Tree().num_nodes() => {Tree().num_nodes()}\n")

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()