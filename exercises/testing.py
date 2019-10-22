# import local modules
import data_structures.linked_list as ll
import data_structures.binary_search_tree as bst
import data_structures.stack as s
import random

def binary_search_tree_test():
    print("## BINARY SEARCH TREE TESTING ##\n")
    print(f"Binary search tree:\n")
    root = bst.node(50)
    for i in range(10):
        root.insert(bst.node(random.randint(0, 100)))
    
    root.print()

    root.insert(bst.node(25))
    root.print()
    print(root.find(25))
    #root.remove(root.left.value)
    root.print()

def linked_list_test():
    print("\n## LINKED LIST TESTING ##\n")
    # appending test
    myList = ll.linked_list()
    print(f"Appending values")
    for i in range(150):
        node = ll.node(random.randint(-i, i))
        myList.append(node)
        print(f"{node.data} appended")
    myList.print()
    print()

    # prepending test
    myList = ll.linked_list()
    print(f"Prepending values")
    for i in range(10):
        node = ll.node(random.randint(-i, i))
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
    [myList.prepend(ll.node(random.randint(0, i))) for i in range(10)]
    print(f"Before sort:", myList, "\n")
    myList.sort()
    print(f"After sort:", myList, "\n")

    # reversing
    print(f"Before reverse:", myList, "\n")
    myList.reverse()
    print(f"After reverse:", myList, "\n")
    myList.reverse()
    print(f"After reverse:", myList, "\n")

def stack_test():
    print("## STACK TESTING ##\n")
    stack = s.Stack(s.Node(100))
    for i in range(100):
        stack.push(random.randint(-100, 100))
    print("Original stack:\n", stack, "\n\n", "Popping following elements:")
    for i in range(25):
        print(stack.pop(), end=" ")
    print("\n\nStack after popping:\n", stack)
    print(f"\nResult of peek:\n{stack.peek()}")
    stack = s.Stack()
    print(f"\nResult of popping an empty stack:\n{stack.pop()}")

def main():
    binary_search_tree_test()
    linked_list_test()
    stack_test()

main()