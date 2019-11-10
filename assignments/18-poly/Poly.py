#  File: Poly.py

#  Description: Assignment 18 | Linked List Representation of Polynomials

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# link class 
class Link (object):
    # link constructor
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    # return str of link object 
    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

# linked list class
class LinkedList (object):
    # linked list constructor
    def __init__ (self):
        self.first = None

    # return str of polynomial linked list object
    def __str__ (self):
        ...

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        ...

    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        ...

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        ...

def main():
# open file poly.txt for reading

# create polynomial p

# create polynomial q

# get sum of p and q and print sum

# get product of p and q and print product

if __name__ == "__main__":
    main()