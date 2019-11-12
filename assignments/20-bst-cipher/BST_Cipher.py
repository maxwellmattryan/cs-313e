#  File: BST_Cipher.py

#  Description: Assignment 20 | Cipher Encryption with Binary Search Trees

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11-12-2019

#  Date Last Modified: 11-12-2019

# Node class
class Node (object):
    # node constructor
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # string representation
    def __str__(self):
        return(f"{self.data}")

    # handle printing
    def print(self):
        if(self != None):
            if(self.left != None):
                self.left.print()
            print(f"{self.data}")
            if(self.right != None):
                self.right.print()

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str=""):
        self.root = None
        [self.insert(char) for char in encrypt_str]

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        if(self.root == None):
            self.root = Node(ch)
        else:
            current = self.root
            while(current != None):
                if(ch == current.data):
                    break
                elif(ch > current.data):
                    if(current.right == None):
                        current.right = Node(ch)
                        break
                    current = current.right
                else:
                    if(current.left == None):
                        current.left = Node(ch)
                        break
                    current = current.left

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        if(self.root != None):
            current = self.root
            str_result = ""
            while(ch != current.data):
                if(ch > current.data):
                    str_result += ">"
                    current = current.right
                else:
                    str_result += "<"
                    current = current.left
                if(current == None):
                    return("")
            if(current == self.root):
                return("*")
            return(str_result)

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        if(self.root != None):
            current = self.root
            for command in st:
                if(command == "*"):
                    return(str(self.root))
                elif(command == "<"):
                    current = current.left
                else:
                    current = current.right
                if(current == None):
                    return("")
            return(current.data)

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        if(self.root != None):
            encrypted_chars = []
            for char in st.lower():
                if(ord(char) == 32 or 96 < ord(char) < 123):
                    encrypted_chars.append(self.search(char))
        return("!".join(encrypted_chars))

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        if(self.root != None):
            decrypted_chars = []
            for letter in st.split("!"):
                decrypted_chars.append(self.traverse(letter))
            return("".join(decrypted_chars))

    # print binary search tree
    def print(self):
        if(self.root != None):
            self.root.print()

def main():
    encryption_key = input("Enter encryption key: ")
    myTree = Tree(encryption_key)
    print()

    encryption_str = input("Enter string to be encrypted: ")
    print(f"Encrypted string: {myTree.encrypt(encryption_str)}\n")

    decryption_str = input("Enter string to be decrypted: ")
    print(f"Decrypted string: {myTree.decrypt(decryption_str)}")

main()