#  File: MagicSquare.py

#  Description: Assignment 01

#  Student's Name: Matthew Maxwell

#  Student's UT EID: mrm5632

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 09-03-2019

#  Date Last Modified: 09-03-2019

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def makeSquare ( n ):
  # creating empty square
  magicSquare = [[0 for i in range(n)] for j in range(n)]
  # printSquare(magicSquare)

  # populating empty square to be magical
  count = 1
  rowIter = len(magicSquare[0]) - 1
  colIter = len(magicSquare[0]) // 2

  # filling
  for i in range(len(magicSquare[0])):
    for j in range(len(magicSquare[0])):
      if(count > len(magicSquare[0]) ** 2):
        break
      if(rowIter >= len(magicSquare[0]) and rowIter == colIter):
        magicSquare[rowIter - 2][colIter - 1] = count
        rowIter -= 1
      elif(rowIter == len(magicSquare[0])):
        magicSquare[0][colIter] = count
        rowIter = 1
        colIter += 1
      elif(colIter == len(magicSquare[0])):
        magicSquare[rowIter][0] = count
        colIter = 1
        rowIter += 1
      else:
          if(magicSquare[rowIter][colIter] == 0):
            magicSquare[rowIter][colIter] = count
          else:
              magicSquare[rowIter - 2][colIter - 1] = count
              rowIter -= 2
              colIter -= 1
          rowIter += 1
          colIter += 1
      count += 1
  return(magicSquare)
  # printSquare(magicSquare)

# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def printSquare ( magicSquare ):
  print("\nHere is a " + str(len(magicSquare)) + " x " + str(len(magicSquare)) + " magic square:\n")
  for i in range(len(magicSquare)):
    row = ""
    for j in range(len(magicSquare[i])):
      row += str(magicSquare[i][j]).rjust(len(str(magicSquare[0][len(magicSquare[0]) // 2])) + 1)
    print(row)
  print()

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def checkSquare ( magicSquare ):
  canonicalSum = int(len(magicSquare) * (((len(magicSquare) ** 2) + 1) / 2))

  rowSum = 0
  columnSum = 0
  diagonalSum = 0
  for i in range(len(magicSquare)):
    for j in range(len(magicSquare[i])):

      # if first row is selected...
      if(i == 0):
        # sum column of j
        for k in range(len(magicSquare[i])):
          columnSum += magicSquare[k][j]
        if(columnSum != canonicalSum):
          print("This is not a magic square")
          return
        columnSum = 0
      
      # checks diagonals
      # top-left to bottom-right diagonal
      if(i == 0 and j == 0):
        for k in range(len(magicSquare[i])):
          diagonalSum += magicSquare[k][k]
        if(diagonalSum != canonicalSum):
          print("This is not a magic square")
          return
        diagonalSum = 0
      elif (i == 0 and j == len(magicSquare[i]) - 1):
        rowIter = i
        colIter = j
        for k in range(len(magicSquare[i])):
          diagonalSum += magicSquare[rowIter][colIter]
          rowIter += 1
          colIter -= 1
        if(diagonalSum != canonicalSum):
          print("This is not a magic square")
          return
        diagonalSum = 0
      
      # but still keeps track of the row sum
      rowSum += magicSquare[i][j]
    if(rowSum != canonicalSum):
      print("This is not a magic square")
      return
    rowSum = 0
  print("This is a magic square and the canonical sum is " + str(canonicalSum))
  return

def isOdd( num ):
  if(num > 0 and num % 2 == 1):
    return(True)
  return(False)

def main():
  # Prompt the user to enter an odd number 1 or greater
  num = eval(input("Please enter an odd number: "))

  # Check the user input
  while(isOdd(num) != True):
    print("ERROR: Invalid number\n")
    num = eval(input("Please enter an odd number: "))

  # Create the magic square
  magicSquare = makeSquare(num)

  # Print the magic square
  printSquare(magicSquare)

  # Verify that it is a magic square
  checkSquare(magicSquare)

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()