#  File: Grid.py

#  Description: Assignment 11 | Greatest Path Sum in a Grid

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 10-07-2019

#  Date Last Modified: 10-13-2019

# counts all the possible paths in a grid recursively
def count_paths (n, row, col):
  if(row == n - 1 or col == n - 1):
    return(1)
  else:
    return(count_paths(n, row + 1, col) + count_paths(n, row, col + 1))

# recursively gets the greatest sum of all the paths in the grid
def path_sum(grid, n, row, col):
  if(row == n - 1 and col == n - 1):
    return(grid[row][col])
  else:
    if(row == n - 1):
      return(grid[row][col] + path_sum(grid, n, row, col + 1))
    elif(col == n - 1):
      return(grid[row][col] + path_sum(grid, n, row + 1, col))
    else:
      return(grid[row][col] + max(path_sum(grid, n, row + 1, col), path_sum(grid, n, row, col + 1)))
    
# dynamic programming solution (can easily find path)
def path_sum_dp(grid, path):
  n = len(grid)
  dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      dp[i][j] = grid[i - 1][j - 1] + max(dp[i][j - 1], dp[i - 1][j])
  i = j = 1
  while(i < n and j < n):
    path.append(grid[i - 1][j - 1])
    if(dp[i][j + 1] > dp[i + 1][j]):
      j += 1
    else:
      i += 1
  while(i < n):
    path.append(grid[i - 1][j - 1])
    i += 1
  while(j < n):
    path.append(grid[i - 1][j - 1])
    j += 1
  path.append(grid[i - 1][j - 1])
  return(dp[n][n])

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
  path = []
  max_path_sum = path_sum(grid, dim, 0, 0)
  max_path_sum = path_sum_dp(grid, path)
  print ('Greatest path sum is', max_path_sum, "\n")
  print(f"Actual path is {path}")

main()