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
    print(f"=== LINKED LIST TESTING ===\n")

    myList = ll.LinkedList()
    size = 10
    
    print("Test 01 - Appending:\n")
    for i in range(size):
        num = random.randint(-size, size)
        print(f"{i}: {num}")
        myList.append(num)
    print(f"\n{myList}\n")

    print("Test 02 - Prepending:\n")
    for i in range(size):
        num = random.randint(-size, size)
        print(f"{i}: {num}")
        myList.prepend(num)
    print(f"\n{myList}\n") 

    print(f"Test 03 - Removing:\n")
    removeIndex = random.randint(0, myList.length - 1)
    removeTarget = myList.get(removeIndex)
    print(f"Removing {removeTarget} ({myList.search(removeTarget)}):")
    myList.remove(removeTarget)
    print(f"\n{myList}\n")

    print(f"Test 04 - Removing At:\n")
    removeIndex = random.randint(0, myList.length - 1)
    removeTarget = myList.get(removeIndex)
    print(f"Removing at i = {removeIndex} ({myList.get(removeIndex)}):")
    myList.removeAt(removeIndex)
    print(f"\n{myList}\n") 

    print(f"Test 05 - Inserting:\n")
    insertIndex = random.randint(0, myList.length)
    insertValue = random.randint(-myList.length, myList.length)
    print(f"Inserting {insertValue} at i = {insertIndex} ({myList.get(insertIndex)}):")
    myList.insert(insertValue, insertIndex)
    print(f"\n{myList}\n")

    print(f"Test 06 - Inserting After:\n")
    insertIndex = random.randint(0, myList.length)
    insertValue = random.randint(-myList.length, myList.length)
    print(f"Inserting {insertValue} after i = {insertIndex} ({myList.get(insertIndex)}):")
    myList.insertAfter(insertValue, insertIndex)
    print(f"\n{myList}\n")

    print(f"Maximum = {myList.maximum()}\n\nMinimum = {myList.minimum()}\n")

    print(f"Test 07 - Reversing:")
    myList.reverse()
    print(f"\n{myList}\n")

    print(f"Test 08 - Sorting:")
    myList.sort()
    print(f"\n{myList}\n")

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
    linked_list_test()

main()