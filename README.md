# CS 313E - Elements of Software Design
## About
This is my repository containing all content related to the course, CS 313E, from the University of Texas at Austin. This course is taught by Dr. Shyamal Mitra and explores algorithms, data structures, object oriented programming paradigms and design concepts. 
## Assignments
This is the bulk of the work. Each assignment subfolder containts a script to run the Python code as well as the html file for accessing the problem in case of the source link being unavailable.
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
10. [Recursion 2 (CodingBat)](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/10-recursion2/Recursion2.py)
    - 8 short but challenging problems exploring recursion. They were taken from [CodingBat's](https://codingbat.com/java/Recursion-2) problem set.
11. [Greatest Path Sum in a Grid](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/11-grid/Grid.py)
    - Given a grid of positive integers, find the greatest path sum in the grid starting from the lop left corner and ending in the bottom right corner. You are only allowed to traverse to the right or down.
12. [(Even) Magic Square](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/12-even-magic-square/EvenMagicSquare.py)
    - In contrast to odd magic squares, even magic squares contain vastly more solutions for each dimension. For example, the solution set for dimension = 4 contains 880 valid grids while the solution set for dimension = 3 contains only 8 valid squares.
13. [Nesting Boxes](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/13-boxes/Boxes.py)
    - Given a set a boxes (list of three dimensions represented by integers), find the largest subset of nesting boxes. A box can nest within another if it's length, width, and height are strictly less than the other box's respective dimension. Boxes are allowed to be rotated, which allows you to rearrange the order of the dimensions. 
14. [Eight Queens Problem](https://github.com/maxwellmattryan/cs-313e/blob/develop/assignments/14-queens/Queens.py)
    - Given a number _n_, denoting the number of queens and the dimension of the chessboard, print all boards containing n queens with each queen in a position so that it cannot capture or be captured by another queen.
## Exams
This folder contains questions and solutions from the three semester exams (there is no final).
- [Exam 01](https://github.com/maxwellmattryan/cs-313e/blob/develop/exams/exam-01.py)
    1. Define a Triangle class (assuming a Point class has been written), with proper methods for perimeter, area, point_inside, and is_isosceles.
    2. Given a grid of 0s and 1s, find the largest rectangle of 1s (use a max area of a histogram)
    3. Given a string, find the longest possible palindrome in the string. 
    4. Given a number n, find x such that x! = n
    5. Get a list of people (represented by letters), pair each one with another in a configuration such that every person's requirement (if there is one) is satisfied.
    6. (Extra credit) - Trace the Ackermann function up to m = 3 and n = 3.
        - A(m, n) = n + 1 if m = 0
        - A(m, n) = A(m - 1, 1) if m > 0 and n = 0
        - A(m, n) = A(m - 1, A(m, n - 1)) if m > 0 and n > 0
## Exercises
This work was not necessary, but I found it helpful to write data structures from scratch along with methods for searching, removing, inserting, sorting, and so forth. To run the code inside this folder:
- [Data Structures](https://github.com/maxwellmattryan/cs-313e/tree/develop/exercises/data_structures)
    - Stacks, Queues
    - Binary Search Trees
    - Linked Lists (+ Doubly-Linked Lists)
- [Algorithms](https://github.com/maxwellmattryan/cs-313e/tree/develop/exercises/algorithms)
    - Sorting (selection, bubble, insertion, merge, quick, and heap)
    - Searching (sequential, binary)
```
cd <path.../cs-313e/exercises>
python testing.py
```
Simply open up the testing script to modify or change any test parameters.  
## Acknowledgements
I am grateful for the amazing opportunity to learn from Dr. Mitra - he was absolutely excellent and I always felt as though I was learning loads from him every class. I fully recommend this class to anyone interested or able to take it. 
   
Thank you very much for reading me !
