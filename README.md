<img align="right" height="35" bottom="0" alt="UT longhorn logo" src="https://upload.wikimedia.org/wikipedia/commons/8/8d/Texas_Longhorns_logo.svg">

#  CS 313E - Elements of Software Design

## Table of Contents

- [About](#about)
- [Assignments](#assignments)
- [Exams](#exams)
- [Exercises](#exercises)
- [Acknowledgments](#acknowledgments)

## About

This is my repository containing all content related from the Fall 2019 semester course, CS 313E, from the University of Texas at Austin. This course is taught by Dr. Shyamal Mitra and explores algorithms, data structures, object oriented programming paradigms and software design concepts. 

## Assignments

1. [(Odd) Magic Sqaure](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/01-magic-square/MagicSquare.py)

    - Create a 3x3 grid of integers such that every row, column, and the two diagonals equal the same number, which is 15 in the case of a 3x3 grid.

2. [Collapsing Intervals](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/02-intervals/Intervals.py)

    - Given a list of intervals (represented by a tuple with starting and ending points), return a modified list of collapsed intervals. In order for two intervals to collapse, the ending point of one must be greater than the starting point of another. For example, the intervals (-10, 0) and (-5, 20) collapse into (-10, 20).

3. [Baby Names](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/03-baby-names/BabyNames.py)

    - Allow for a user to query a database of the 1000 most popular names in the United States per decade. 
    
4. [Word Search](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/04-word-search/WordSearch.py)

    - Given a file with a word search (grid of letters) and a list of words, write a program that returns each word in the list if it was found in the search. Remember that words can be valid whether they are represented backwards, diagonally, upside down, etc in the grid.

5. [Basic Geometry](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/05-geom/Geom.py)

    - Familiarize yourself with Python and object oriented programming concepts. Create basic classes and methods for Point, Circle, Rectangle, and Triangle objects.

6. [Office Space](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/06-office-space/OfficeSpace.py)

    - Imagine that your workplace is moving to a new location and everyone requests a specific amount and the location of their new personal office space. Find the total amounts of unallocated and contested office space and the guaranteed space allowed for each employee.

7. [Convex Hull](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/07-convex-hull/ConvexHull.py)

    - A convex hull is the smallest convex polygon that encloses a certain set of points. Given a file of coordinates, find the points that comprise the convex hull solution.

8. [Work 'Till You Drop](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/08-work/Work.py)

    - The scenario is that it's late at night, and you have to write n lines of code before the morning. After writing _v_ lines of code, you drink a cup of coffee to regain some energy,but it actually reduces your productivity so that you only write _v // k ** 1_ new lines of code. After another cup, you can only write _v // k ** 2_. Find the lowest amount of _v_ lines of code so that you can write at least _n_ lines of code where _1 ≤ n ≤ 10^6_ and _2 ≤ k ≤ 10_.

9. [Crossing the Bridge](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/09-bridge/Bridge.py)

    - There are _n_ people who wish to cross a bridge at night. Only two people may cross the bridge at any time and they must have a flashlight to get across. After a pair crosses, a person must come back so that the people still needing to cross have the flashlight. Also, each person crosses the bridge a different speed so the crossing time of a pair of people is determined by the slower one's time. Find the minimum time in which everyone can cross the bridge.

10. [Recursion 2 (CodingBat)](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/10-recursion2/recursion2.py)

    - 8 short but challenging problems exploring recursion. They were taken from [CodingBat's](https://codingbat.com/java/Recursion-2) problem set.

11. [Greatest Path Sum in a Grid](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/11-grid/Grid.py)

    - Given a grid of positive integers, find the greatest path sum in the grid starting from the lop left corner and ending in the bottom right corner. You are only allowed to traverse to the right or down.

12. [(Even) Magic Square](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/12-even-magic-square/EvenMagicSquare.py)

    - In contrast to odd magic squares, even magic squares contain vastly more solutions for each dimension. For example, the solution set for dimension = 4 contains 880 valid grids while the solution set for dimension = 3 contains only 8 valid squares.

13. [Nesting Boxes](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/13-boxes/Boxes.py)

    - Given a set a boxes (list of three dimensions represented by integers), find the largest subset of nesting boxes. A box can nest within another if it's length, width, and height are strictly less than the other box's respective dimension. Boxes are allowed to be rotated therefore the order of dimensions representing a single box does not matter.

14. [Eight Queens Problem](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/14-queens/Queens.py)

    - Given a number _n_, denoting the number of queens and the dimension of the chessboard, print all boards containing n queens with each queen in a position so that it cannot capture or be captured by another queen.

15. [Reducible Words](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/15-reducible-words/Reducible.py)

    - What is the longest English word that remains a valid English word as you remove one letter at a time from it? Once only one letter is left, it is only valid if it is "a", "i", or "o". Such words are known as reducible words. Consider the example, "string":
    
        - _string -> sting -> sing -> sin -> in -> i_

    - Given a list of valid English words (roughly 113,809 entries), write a program that finds the longest reducible word(s). To solve this problem optimally, the solution __must__ implement hashing.

16. [Singly Linked List](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/16-singly-linked-list/TestLinkedList.py)

    - Write the various methods for a linked list implementation in Python (such as insertion, deletion, removal, sorting, copying, merging, searching, and so forth) and test them. Assume that the data you are handling is just integers for now (for easier comparisons with no errors in floating point precision). 

17. [Josephus Problem (Circularly Linked List)](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/17-josephus/Josephus.py)

    - The Josephus problem is as follows: there is a group of soldiers surrounded by an overwhelming enemy force. There is no hope for victory, so they make a pact to commit suicide. They stand in a circle and starting from a randomly selected solider, they count _n_ soliders. That soldier is killed by the starting solider and the count begins again from the next solider after. One by one, each solider is killed until one is standing who is free to join the enemy forces.

    - Given an input file with total number of solders, the starting solider, and _n_, write a program that determines the last solider alive using an implementation of a linked list.

18. [Polynomial Operations w/ Linked Lists](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/18-poly/Poly.py)

    - Assuming that the polynomials given will have non-zero integer coefficients and exponents are greater than zero, define a Linked List (and Link) class that represents a polynomial. You will be given a file, [poly.txt](https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/poly.txt), containing data for just two polynomials. The first line will represent the number of given terms, _n_, for the first polynomial followed by _n_ lines. Each line has two integers separated by a space, with the first int representing the coefficient and the second representing the exponent. Following this will be a blank line, then the exact same format for the second polynomial.

    - Create a linked list of terms that contain the coefficient, exponent, and pointer to the next term. Then write methods to multiply and add polynomials together (do not forget a simplify / reduce method).

19. [Expression Tree](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/19-expression-tree/ExpressionTree.py)

    - Given a valid mathematical expression in infix notation, create an expression tree. Write methods that evaluate the expression and also print the prefix and postfix notation equivalent. 

20. [Cipher Encryption / Decryption with Binary Search Tree](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/20-bst-cipher/BST_Cipher.py)

    - Write a program that will encrypt / decrypt string inputs based on a given encryption key. First create a BST comprised of unique set of letters in the encryption key. To encrypt a string, change each character's representation to the specific traversal moves required to get the character. To decrypt, simply follow the given directions in the input.

21. [Binary Tree](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/21-binary-trees/TestBinaryTree.py)

    - Given the [Node and Tree class partly developed in class](https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/notes/Lect08Nov.txt), complete the implementation and write the following methods:

        - is_similar(other) => True if two trees are the same, False otherwise
        - print_level(level) => prints all nodes on level or nothing if level does not exist
        - get_height() => height of binary tree
        - num_nodes() => total number of nodes in binary tree

22. [Graph Traversal](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/22-graph-traversal/Graph.py)

    - Given a file, [graph.txt](https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/graph.txt), write various methods for graphs (searching (breadth-first, depth-first), adding, removing, etc.). 

23. [Topological Sort and Cycle Detection](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/23-topological-sort/TopoSort.py)

    - Given a graph from an input .gif file and a txt file, create a Graph object with all vertices and edges properly notated in an adjacency matrix. From here, write two methods: one that returns true if a graph has a cycle and false otherwise, and one that topologically sorts the graph (which can only happen if the graph does __NOT__ have a cycle).

24. [Greatest Path Sum in Triangle](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/24-triangle-path-sum/Triangle.py)

    - Use the four algorithm paradigms (brute force, divide and conquer, greedy, and dynamic programming) to calculate the greatest sum path from the top to the bottom from a given input file:  
    
        3  
        75  
        94 62  
        37 43 99  
    
    - The first line denotes _n_ number of rows in the triangle. The next following _n_ lines of data will have only positive integers greater than 0. The first line of data in the triangle will have only one number, the second line in the triangle will have two, and so on. The _n<sup>th</sup>_ line will have _n_ integers.

## Exams
- [Exam 01](https://github.com/maxwellmattryan/cs-313e/blob/develop/exams/exam-01.py)

    1. Define a Triangle class (assuming a Point class has been written), with proper methods for perimeter, area, point_inside, and is_isosceles.

    2. Given a grid of 0s and 1s, find the largest rectangle of 1s (use a max area of a histogram).

    3. Given a string, find the longest possible palindrome in the string. 

    4. Given a number n, find x such that x! = n.

    5. Get a list of people (represented by letters), pair each one with another in a configuration such that every person's requirement (if there is one) is satisfied.

    6. (Extra credit) - Trace the Ackermann function up to m = 3 and n = 3.

        - A(m, n) = n + 1 if m = 0
        - A(m, n) = A(m - 1, 1) if m > 0 and n = 0
        - A(m, n) = A(m - 1, A(m, n - 1)) if m > 0 and n > 0

- [Exam 02](https://github.com/maxwellmattryan/cs-313e/blob/develop/exams/exam-02.py)

    1. Given a doubly linked list, write an insert_in_order and delete method using a provided implementation of a DoubleLink.

    2. Implement a hash table that uses separate chaining to hash and store names. Use a LinkedList at each index to accomplish this and to avoid linear probing.

    3. Given a string of tokens of an expression, write a function that returns True if that expression is valid. An expression is valid if its brackets are properly nested, meaning a pair of brackets is opened and closed __within__ another.

    4. Given both a sequence of pushes and pops to make to the stack, determine if the two sequences are a valid possible push / pop combination. 

    5.  Given a stack of pancakes, sort the pancakes in increasing order only by flipping either a pancake or a stack of pancakes on top of the unflipped pancakes.

    6. (Extra credit) - Fill out the expression building table for (2 + 3) * 4 using the four of the expression types: 

        - A (add expression)
        - M (multiply expression)
        - P (parenthetical expression)
        - N (integer)

- [Exam 03](https://github.com/maxwellmattryan/cs-313e/blob/develop/exams/exam-03.py)

    - Choose __two__ of the following:

        1. A perfect binary tree is a binary tree in which all interior nodes have two children and all leaf nodes have the same depth. Given a binary tree, write a method that returns True if is perfect and False otherwise. The Node and Tree classes have been defined, and you may write a helper method if you wish.

        2. Given a sorted list of integers write a method to create a balanced binary search tree. The list contains the proper number of elements to create a balanced tree.

        3. Given an undirected graph and a starting vertex _x_, print all of the vertex labels within a distance _k_ (the number of vertices needed to travel through in order to reach your destination) from the starting vertex. The Vertex and Graph classes have been defined, and you may not use helper methods.

        4. Given a binary search tree, write a method to print its inorder traversal without using recursion. Use a stack to help achieve this. You may assume the Stack class has been defined with methods for push(), pop(), and peek().
        
        5. Implement the Graph class using only an adjacency list rather than an adjacency matrix. The adjacency list shall be a list of dictionaries, with the first one referring to the edges starting from the first vertex and so on. The key for each key-value pair is the ending vertex, and the value is the weight of this edge.

    - Choose __one__ of the following:

        6. Answer both parts:

            - Using the given [graph](./), following Kruskal's algorithm, list the edges in the order that they would be added to form the minimum spanning tree.
            - Repeat the above step, but use Prim's algorithm and start on vertex C 

        7. Add the list below to an empty AVL tree.
            - [3, 9, 4, 5, 32, 29, 16, 31, 1, 77, 7]
            - What would the tree look look when you add 5?
            - What would the tree look like when you add all elements?
            - Why do we use self-balancing trees, and what are the benefits?
        
        8. Add the list below to an empty max-heap.
            - [3, 9, 4, 5, 32, 29, 16, 31, 1, 77, 7]
            - What would the heap look look when you add 5?
            - What would the heap look like when you add all elements?
            - Why do we use max-heaps, and what are the benefits?
    <br/><br/>
    9. Using Dijkstra's shortest path algorithm, find the shortest paths from vertex D to all the other vertices in the above graph.

    10. (Extra credit) - You have a set of bottles with different volumes filled with your favorite drink. You may drink as much as you want with the constraint that you cannot drink from two adjacent bottles. How can you maximize your intake? Manually fill the table with columns for the index, volume, and s(v) - the largest sum so far - and then write the code to do the same.

## Exercises
- [Data Structures](https://github.com/maxwellmattryan/cs-313e/tree/develop/exercises/data_structures)

    - Stacks, queues
    - Trees (binary search trees, expression trees, and decision trees)
    - Linked lists (singly, doubly, and circularly-linked)
    - Hash tables
    - Graphs (direct / undirect, weighted / unweighted, connected / unconnected, complete / incomplete, cyclic / acyclic, bipartite)

- [Algorithms](https://github.com/maxwellmattryan/cs-313e/tree/develop/exercises/algorithms)

    - Sorting (selection, bubble, insertion, merge, quick, heap, radix, topological)
    - Searching (sequential, binary, depth-first, breadth-first)
    - Hashing (linear probing, quadratic probing, double hashing)
    - Graph-related (Dijkstra's, Prim's, Kruskal's, cycle / path detection (Eulerian and Hamiltonian))
    - Dynamic programming 
    
### Instructions

These scripts are imported into a testing script as modules. Their tests are located within the testing.py script, which is where you can test any functionality of the particular data structure or algorithm.

```
cd <path-to/cs-313e/exercises>
python testing.py
``` 

## Acknowledgments

I am grateful for the amazing opportunity to learn from Dr. Mitra - he was absolutely excellent and I always felt as though I was learning loads from him every class. I fully recommend this class to anyone interested or able to take it. The work and effort is worth it.
   
Thank you very much for reading !

[back to top &#8593;](#cs-313e---elements-of-software-design)
