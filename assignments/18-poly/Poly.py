#  File: Poly.py

#  Description: Assignment 18 | Linked List Representation of Polynomials

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11-10-2019

#  Date Last Modified: 11-10-2019

# link class 
class Link (object):
    # link constructor
    def __init__ (self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    # return str of link object 
    def __str__ (self):
        return(f"({self.coeff}, {self.exp})")

# linked list class
class LinkedList (object):
    # linked list constructor
    def __init__ (self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    # return str of polynomial linked list object
    def __str__ (self):
        if(self.head == None):
            return("")
        current = self.head
        poly_string = f"{current}"
        while(current.next != None):
            current = current.next
            poly_string += f" + {current}"
        return(poly_string)

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        self.length += 1
        new = Link(coeff, exp)
        if(self.head == None):
            self.head = self.tail = new
        else:
            prev = current = self.head
            while(current.exp >= exp):
                prev = current
                current = current.next
                if(current == None):
                    prev.next = new
                    self.tail = new
                    return
            if(current == self.head):
                new.next = current
                self.head = new
            else:
                prev.next = new
                new.next = current

    # add polynomial other to this polynomial and return the sum
    def add (self, other):
        if(self.head == None):
            return(other)
        elif(other.head == None):
            return(self)
        else:
            sum_list = LinkedList()
            ptr_self = self.head
            ptr_other = other.head
            # merge 
            while(ptr_self != None and ptr_other != None):
                if(ptr_self.exp == ptr_other.exp):
                    sum_list.insert_in_order((ptr_self.coeff + ptr_other.coeff), ptr_self.exp)
                    ptr_self = ptr_self.next
                    ptr_other = ptr_other.next
                elif(ptr_self.exp > ptr_other.exp):
                    sum_list.insert_in_order(ptr_self.coeff, ptr_self.exp)
                    ptr_self = ptr_self.next
                else:
                    sum_list.insert_in_order(ptr_other.coeff, ptr_other.exp)
                    ptr_other = ptr_other.next            
            # check for leftover terms in both lists
            while(ptr_self != None):
                sum_list.insert_in_order(ptr_self.coeff, ptr_self.exp)
                ptr_self = ptr_self.next
            while(ptr_other != None):
                sum_list.insert_in_order(ptr_other.coeff, ptr_other.exp)
                ptr_other = ptr_other.next 
            return(sum_list)

    # multiply polynomial other to this polynomial and return the product
    def mult (self, other):
        if(self.head == None):
            return(other)
        elif(other.head == None):
            return(self)
        else:
            product_list = LinkedList()
            ptr_self = self.head
            while(ptr_self != None):
                ptr_other = other.head
                while(ptr_other != None):
                    n_coeff = ptr_self.coeff * ptr_other.coeff
                    n_exp = ptr_self.exp + ptr_other.exp
                    product_list.insert_in_order(n_coeff, n_exp)
                    ptr_other = ptr_other.next
                ptr_self = ptr_self.next
            return(product_list)

    # simplify if possible the terms in a polynomial
    def simplify(self):
        if(self.head != None):
            current = self.head
            while(current != None):
                n_ptr = current.next
                while(n_ptr != None and n_ptr.exp == current.exp):
                    current.coeff += n_ptr.coeff
                    current.next = n_ptr.next
                    n_ptr = n_ptr.next
                current = current.next

# return polynomials p and q as linked lists with data from poly.txt
def get_poly_input():
    # helper function for creating the list from data
    def create_list(num_terms, my_file):
        my_list = LinkedList()
        for i in range(num_terms):
            coeff, exp = [int(token) for token in my_file.readline().strip().split(" ")]
            my_list.insert_in_order(coeff, exp)
        return(my_list)

    my_file = open("./poly.txt")
    num_terms = int(my_file.readline())
    p = create_list(num_terms, my_file)
    my_file.readline()
    num_terms = int(my_file.readline())
    q = create_list(num_terms, my_file)
    return(p, q)

def main():
    # open file poly.txt for reading, get polynomial linked lists
    p, q = get_poly_input()

    # get sum of p and q and print sum
    sum_list = p.add(q)
    print(f"Sum: {sum_list}\n")

    # get product of p and q and print product
    mult_list = p.mult(q)
    mult_list.simplify()
    print(f"Product: {mult_list}")

if __name__ == "__main__":
    main()