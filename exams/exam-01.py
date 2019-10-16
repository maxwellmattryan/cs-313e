# dependencies
import math

# Array printing method
def printArr(arr):
    [print(row) for row in arr]
    print()

# Q1:
# Define a Triangle class (assume Point class is written)
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, other):
        return(math.hypot(self.x - other.x, self.y - other.y))

class Triangle(object):
    def __init__(self, v1_x=0, v1_y=0, v2_x=1, v2_y=0, v3_x=0, v3_y=1):
        self.v1 = Point(v1_x, v1_y)
        self.v2 = Point(v2_x, v2_y)
        self.v3 = Point(v3_x, v3_y)

    def perimeter(self):
        return(-1)

    def area(self):
        a = self.v1.dist(self.v2)
        b = self.v1.dist(self.v3)
        return(a * b * 0.5)
    
    def isRight(self):
        return(-1)

    def pointInside(self, p):
        return(-1)
    
# Q2:
# Given a grid of 0s and 1s, find the largest rectangle
# of 1s in the grid (using histograms)
def largestRectangle(grid):
    # get maximum area of histogram
    def maxAreaInHistogram(hist):
        stack = []
        largest = 0
        for index, height in enumerate(hist):
            last = None
            while(stack and stack[-1][1] > height):
                last = stack.pop()
                largest = max(largest, (index - last[0]) * last[1])
            if last is not None:
                stack.append((last[0], height))
            else:
                stack.append((index, height))
        index = len(hist)
        while stack:
            last = stack.pop()
            largest = max(largest, (index - last[0]) * last[1])
        return(largest)

    # convert grid into histogram
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == 1):
                grid[i][j] = grid[i - 1][j] + 1

    # find maximum area of each row of new histogram grid
    maxArea = max([maxAreaInHistogram(row) for row in grid])
    return(maxArea)


# Q3:
# Given a string, what is the longest possible palindrome
# within the string
# todo : can this be implemented faster using binary search algorithm
def longestPalindrome(string):
    # helper method to determine if string is a palindrome
    def isPalindrome(string):
        if(len(string) % 2 == 0):
            return(False)
        left = right = len(string) // 2
        while(left >= 0 and right < len(string)):
            if(string[left] != string[right]):
                return(False)
            left -= 1
            right += 1
        return(True)

    string = string.replace(" ", "")
    if(isPalindrome(string)):
        return(string)
    maxPalindrome = ""
    for Len in range(1, len(string)):
        for i in range(len(string) - Len + 1):
            j = i + Len - 1
            tempString = ""
            for k in range(i, j + 1):
                tempString += string[k]
            if(isPalindrome(tempString) and len(tempString) > len(maxPalindrome)):
                maxPalindrome = tempString
    return(maxPalindrome)

# Q4:
# Given a number, n, find x such that factorial(x) == n
def inverseFactorial(n):
    if(n == 1 or n == 2):
        return(n)
    lo = 0
    hi = n // 2
    while(lo < hi):
        x = (lo + hi) // 2
        xF = math.factorial(x)
        if(xF == n):
            return(x)
        elif(xF > n):
            hi = x
        else:
            lo = x
    return(-1)

# Q5 :
# Given a set of people, create pairings such that everyone's requirements are satisfied
def findPairings():
    print(f"Q5: Fix me\n")
    return(-1)

# EC:
# Trace Ackermann's function
# if m = 0, A(m, n) => n + 1
# if m > 0 and n = 0, A(m, n) => A(m - 1, 1)
# if m > 0 and n > 0, A(m, n) => A(m - 1, A(m, n - 1))
def ackermann(m, n):
    if(m == 0):
        return(n + 1)
    else:
        if(n == 0):
            return(ackermann(m - 1, 1))
        else:
            return(ackermann(m - 1, ackermann(m, n - 1)))

def main():
    # Q1 - Python classes
    myTriangle = Triangle(0, 0, 2, 0, 0, 2)
    print(f"Q1: Fix me\n")

    # Q2 - Largest rectangle of 1s
    myArr = [
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1]
    ]
    print(f"Q2: The largest rectangle is {largestRectangle([[num for num in row] for row in myArr])} units\n")
    printArr(myArr)

    # Q3 - Longest palindrome in string
    myString = "asdaibohphobia"
    print(f"Q3: The longest palindrome in \"{myString}\" is \"{longestPalindrome(myString)}\"\n")

    # Q4 - Inverse factorial of integer
    n = 4
    n = math.factorial(n)
    print(f"Q4: The inverse factorial of {n} is {inverseFactorial(n)}\n")

    # Q5 - Subset problem
    print(f"{findPairings()}")

    # EC - Ackermann's function trace (n = 3)
    n = 4
    myGrid = [[ackermann(i, j) for j in range(n)] for i in range(n)]
    print(f"EC: The Ackermann function traced up to n = {n}\n")
    printArr(myGrid)

main()