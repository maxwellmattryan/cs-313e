#  File: EvenMagicSquare.py

#  Description: Assignment 12 | Even Magic Square

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 10-13-2019

#  Date Last Modified: 10-13-2019

import math

# Permute through a list => O(n!)
def permute(a, lo):
    hi = len(a)
    n = int(math.sqrt(hi))
    magicConst = (n * ((n ** 2) + 1)) / 2
    # if lo equals hi, then all values have been swapped 
    if(lo == hi):
        grid = convert(a)
        if(isMagicSquare(grid)):
            printGrid(grid) 
    else:
        # todo: SMART OPTIMIZATIONS GO HERE !
        # maybe this should be a while loop ... ?
        i = lo
        while(i < hi):
            if(i == 0 or (i % n == 0 and i > 0)):
                rowSum = sum([a[i + j] for j in range(n)])
                print(f"{[a[i + j] for j in range(n)]} => Row sum = {rowSum} and magic constant = {magicConst}")
                if(rowSum == magicConst):
                    print(f"Good row")
                    i += n
                else:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    permute(a, lo + 1)
                    a[i], a[i + 1] = a[i + 1], a[i]
            else:
                a[lo], a[i] = a[i], a[lo]
                permute(a, lo + 1)
                a[lo], a[i] = a[i], a[lo]
            i += 1

# Convert 1D to 2D => ?
def convert(myList):
    n = int(math.sqrt(len(myList)))
    myGrid = [[myList[i + j] for j in range(n)] for i in range(0, n ** 2, n)]
    return(myGrid)

# Check if grid is valid magic square
def isMagicSquare(grid):
    n = len(grid)
    magicConst = (n * ((n ** 2) + 1)) / 2
    # check rows and columns
    for i in range(n):
        rowSum = 0
        for j in range(n):
            rowSum += grid[i][j]
            if(i == 0):
                colSum = 0
                for k in range(n):
                    colSum += grid[k][j]
                if(colSum != magicConst):
                    return(False)
        if(rowSum != magicConst):
            return(False)
    diag1 = diag2 = 0
    for i in range(n):
        diag1 += grid[i][i]
        diag2 += grid[-1 * (i + 1)][i]
    if(diag1 != magicConst or diag2 != magicConst):
        return(False)
    return(True)

# Print grid => O(n)
def printGrid(grid):
    [print(row) for row in grid]
    print()

def main():
    # Create 1D list of integers 1-16
    myList = [i + 1 for i in range(9)]
    print(f"1D : {myList}")

    # Permute this list (and print all valid magic squares)
    permute(myList, 0)

main()