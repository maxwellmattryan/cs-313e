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
        if(level < 1):
            return
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
        if(self.root == None):
            return (-1)
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
    tree_a = Tree()
    tree_b = Tree()
    tree_c = Tree()

    # Create two extra trees for testing (an empty tree and a tree with only one element)
    tree_zero = Tree()
    tree_one = Tree()
    tree_one.insert(random.randint(-1000000, 1000000))

    # initialize tree size
    size = 120

    # insert same random element into tree_a and tree_b and different one into tree_c (which will *probably* cause a different height)
    for i in range(size):
        rand_num = random.randint(-size, size)
        tree_a.insert(rand_num)
        tree_b.insert(rand_num)
        tree_c.insert(random.randint(-size, size))

    # Test your method is_similar()
    print(f"TEST: is_similar")
    print(f"tree_a.is_similar(tree_a) => {tree_a.is_similar(tree_a)}")
    print(f"tree_a.is_similar(tree_b) => {tree_a.is_similar(tree_b)}")
    print(f"tree_a.is_similar(tree_c) => {tree_a.is_similar(tree_c)}")
    print(f"tree_a.is_similar(tree_one) => {tree_a.is_similar(tree_one)}")
    print(f"tree_a.is_similar(tree_zero) => {tree_a.is_similar(tree_zero)}")
    print(f"tree_one.is_similar(tree_a) => {tree_one.is_similar(tree_a)}")
    print(f"tree_one.is_similar(tree_one) => {tree_one.is_similar(tree_one)}")
    print(f"tree_one.is_similar(tree_zero) => {tree_one.is_similar(tree_zero)}")
    print(f"tree_zero.is_similar(tree_a) => {tree_zero.is_similar(tree_a)}")
    print(f"tree_zero.is_similar(tree_one) => {tree_zero.is_similar(tree_one)}")
    print(f"tree_zero.is_similar(tree_zero) => {tree_zero.is_similar(tree_zero)}\n")

    # Print the various levels of two of the trees that are different
    print(f"TEST: print_level")
    print("tree_a, tree_b:")
    for i in range(1, tree_a.get_height() + 2):
        print(f"L{i}:", end=" ")
        tree_a.print_level(i)
        print()
    
    print("\ntree_c:")
    for i in range(1, tree_c.get_height() + 2):
        print(f"L{i}:", end=" ")
        tree_c.print_level(i)
        print()
    print(f"\ntree_c.print_level(-5) =>", end=" ")
    tree_c.print_level(-5)
    print(f"\ntree_c.print_level(0) =>", end=" ")
    tree_c.print_level(0)
    print(f"\ntree_c.print_level(1) =>", end=" ")
    tree_c.print_level(1)
    random_level = random.randint(1, tree_c.get_height() + 1)
    print(f"\ntree_c.print_level({random_level}) =>", end=" ")
    tree_c.print_level(random_level)
    print()

    print(f"\ntree_one.print_level(1) =>", end=" ")
    tree_one.print_level(1)
    print()
    print(f"tree_one.print_level(2) =>", end=" ")
    tree_one.print_level(2)
    print("\n")

    print(f"tree_zero.print_level(0) =>", end=" ")
    tree_zero.print_level(0)
    print()
    print(f"tree_zero.print_level(1) =>", end=" ")
    tree_zero.print_level(1)
    print("\n")

    # Get the height of the two trees that are different
    print(f"TEST: get_height")
    print(f"tree_a.get_height() => {tree_a.get_height()}")
    print(f"tree_b.get_height() => {tree_b.get_height()}")
    print(f"tree_c.get_height() => {tree_c.get_height()}")
    print(f"tree_one.get_height() => {tree_one.get_height()}")
    print(f"tree_zero.get_height() => {tree_zero.get_height()}\n")

    # Get the total n
    print(f"TEST: num_nodes")
    print(f"tree_a.num_nodes() => {tree_a.num_nodes()}")
    print(f"tree_b.num_nodes() => {tree_b.num_nodes()}")
    print(f"tree_c.num_nodes() => {tree_c.num_nodes()}")
    print(f"tree_one.num_nodes() => {tree_one.num_nodes()}")
    print(f"tree_zero.num_nodes() => {tree_zero.num_nodes()}\n")

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()