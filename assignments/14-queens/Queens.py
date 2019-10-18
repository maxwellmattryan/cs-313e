#  File: Queens.py

#  Description: Assignment 14 | Queens  

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10-18-2019

#  Date Last Modified: 10-18-2019

# define queens class
class Queens(object):
    # initialize the board
    def __init__(self, n=4):
        self.n = n
        self.board = [["*" for j in range(self.n)] for i in range(self.n)]

    # print the board
    def printBoard(self):
        [print(row) for row in self.board]
        print()

    # check if no queen will defeat another
    def isValid(self, row, col):
        # check rows and columns for validity
        for i in range(self.n):
            if(self.board[row][i] == "Q" or self.board[i][col] == "Q"):
                return(False)
        # check diagonals for validity
        for i in range(self.n):
            for j in range(self.n):
                rowDiff = abs(row - i)
                colDiff = abs(col - j)
                if(rowDiff == colDiff and self.board[i][j] == "Q"):
                    return(False)
        return(True)

    # recursively solve via backtracking
    def recursiveSolve(self, col, solutions):
        if(col == self.n):
            solutions.append(self.board)
            return(True)
        else:
            for i in range(self.n):
                if(self.isValid(i, col)):
                    self.board[i][col] = "Q"
                    if(self.recursiveSolve(col + 1, solutions)):
                        return(True)
                    self.board[i][col] = "*"
            return(False)
            
    # print board if solution exists
    def solve(self):
        solutions = []
        for i in range(self.n):
            if(self.recursiveSolve(i, solutions)):
                self.printBoard() 
        return(solutions)   

def main():
    # prompt user to enter size of the board
    n = int(eval(input("Enter the size of the board: ")))
    while(n < 1 or n > 8):
        n = eval(input("Enter the size of the board: "))
    print()

    # create chess board
    game = Queens(n)

    # find the solution(s), return an array of solution
    solutions = game.solve()

    # final print statement 
    print(f"There are {len(solutions)} solutions for a {n} x {n} board.")

main()