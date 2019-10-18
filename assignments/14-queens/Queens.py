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
        self.solutions = []
        self.board = [["*" for j in range(self.n)] for i in range(self.n)]

    # print the board
    def __str__(self):
        count = 0
        for solution in self.solutions:
            count += 1
            for row in solution:
                print(f"{' '.join(row)}")
            if(count < len(self.solutions)):
                print()
        return("")

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
            
    # print board if solution exists
    def solve(self, col):
        if(col == self.n):
            self.solutions.append([[self.board[i][j] for j in range(self.n)] for i in range(self.n)])
        else:
            for i in range(self.n):
                if(self.isValid(i, col)):
                    self.board[i][col] = "Q"
                    self.solve(col + 1)
                    self.board[i][col] = "*"

# store solutions into file named "solutions-<dimenion>.txt"
def storeData(dimension, solutions):
    myFile = open(f"solutions-{dimension}.txt", "w")
    for i in range(len(solutions)):
        myFile.write(f"Solution {i + 1:0{len(str(len(solutions)))}d}\n")
        [myFile.write(" ".join(row) + "\n") for row in solutions[i]]
        myFile.write("\n")
    myFile.close()

def main():

    # prompt user to enter size of the board
    n = int(eval(input("Enter the size of the board: ")))
    while(n < 1 or n > 100):
        n = eval(input("Enter the size of the board: "))
    print()

    # create chess board
    game = Queens(n)

    # find the solution(s)
    game.solve(0)

    # print solutions and final program statement
    print(f"{game}\nThere are {len(game.solutions)} solutions for a {n} x {n} board.")

    # store solutions into file
    storeData(n, game.solutions)

main()