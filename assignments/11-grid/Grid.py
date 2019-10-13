#  File: Grid.py

#  Description: Assignment 11 | Greatest Path Sym in a Grid

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 10-07-2019

#  Date Last Modified: 10-11-2019

# counts all the possible paths in a grid recursively
def count_paths (n, row, col):
  if(row == n - 1 or col == n - 1):
    return(1)
  else:
    return(count_paths(n, row + 1, col) + count_paths(n, row, col + 1))

# recursively gets the greatest sum of all the paths in the grid
def path_sum (grid, n, row, col):
  pathSum = 0
  return(pathSumHelper(grid, n, row, col, pathSum))

def pathSumHelper(grid, n, row, col, mySum):
  if(row == n - 1):
    while(col < n):
      mySum += grid[row][col]
      col += 1
    return(mySum)
  elif(col == n - 1):
    while(row < n):
      mySum += grid[row][col]
      row += 1
    return(mySum)
  else:
    mySum += grid[row][col]
    if(grid[row + 1][col] < grid[row][col + 1]):
      col += 1
    else:
      row += 1
    return(pathSumHelper(grid, n, row, col, mySum))
    
def main():
  # open file for reading
  in_file = open ("./grid.txt", "r")

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)

  # create an empty grid
  grid = []

  # populate the grid
  for i in range (dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append (row)

  # close the file
  in_file.close()

  # get the number of paths in the grid and print
  num_paths = count_paths (dim, 0, 0)
  print ('Number of paths in a grid of dimension', dim, 'is', num_paths)
  print ()

  # get the maximum path sum and print
  max_path_sum = path_sum (grid, dim, 0, 0)
  print ('Greatest path sum is', max_path_sum)

main()