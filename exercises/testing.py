import data_structures as ds
import random

def linked_list_test():
    # appending test
    myList = ds.linked_list.linked_list()
    print(f"Appending values")
    for i in range(10):
        node = ds.linked_list.node(random.randint(-i, i))
        myList.append(node)
        print(f"{node.data} appended")
        myList.print()
    print()

    # prepending test
    myList = ds.linked_list.linked_list()
    print(f"Prepending values")
    for i in range(10):
        node = ds.linked_list.node(random.randint(-i, i))
        myList.prepend(node)
        print(f"{node.data} prepended")
        myList.print()
    print()

    # removal test 
    print(f"Removing values")
    for i in range(5):
        myList.print()
        print(f"{myList.head} removed")
        myList.remove(None)
    print()

    # recursive traversal
    print(f"Traversing recursively...")
    myList.print_recursive(myList.head)
    print()

    # finding index of value
    print(f"Index of 3 = {myList.index_of(3)}\n")

    # finding value at index
    n = len(myList)
    print(f"Length of linked list = {n}")
    print(f"Value at {n // 2} = {myList.get(n // 2)}\n")

    # clear all elements
    print(f"Before clearing: ", end="")
    myList.print()
    myList.clear()
    print(f"After clearing: ", end="")
    myList.print()
    print()

    # sorting
    [myList.prepend(ds.linked_list.node(random.randint(0, i))) for i in range(10)]
    print(f"Before sort:", myList, "\n")
    myList.sort()
    print(f"After sort:", myList, "\n")

    # reversing
    print(f"Before reverse:", myList, "\n")
    myList.reverse()
    print(f"After reverse:", myList, "\n")
    myList.reverse()
    print(f"After reverse:", myList, "\n")

def binary_tree_test():
    print(f"Binary tree")
    root = ds.binary_tree.node(50)
    root.left = ds.binary_tree.node(25)
    root.left.left = ds.binary_tree.node(12.5)
    root.left.right = ds.binary_tree.node(37.5)
    root.right = ds.binary_tree.node(75)
    root.right.left = ds.binary_tree.node(62.5)
    root.right.right = ds.binary_tree.node(87.5)
    root.print()

def main():
    #linked_list_test()
    binary_tree_test()

main()