#  File: Triangle.py

#  Description: Assignment 24 | Greatest Path Sum in a Triangle

#  Student's Name: Matthew Maxwell

#  Student's UT EID: mrm5632

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 12-02-2019

#  Date Last Modified: 12-05-2019

# DEPENDENCIES
import time
import random

# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    memo = []
    def exhaustive_search_helper(grid, total_sum, row, col, memo):
        total_sum += grid[row][col]
        if row == len(grid) - 1:
            memo.append(total_sum)
        else:
            exhaustive_search_helper(grid, total_sum, row + 1, col, memo)
            exhaustive_search_helper(grid, total_sum, row + 1, col + 1, memo)
    exhaustive_search_helper(grid, 0, 0, 0, memo)
    memo.sort()
    return memo[-1]

# returns the greatest path sum using greedy approach
def greedy (grid):
    row_index = 1
    triangle_ptr = 0
    greatest_path_sum = grid[0][triangle_ptr]
    while(row_index < len(grid) and triangle_ptr < len(grid[row_index]) - 1):
        if grid[row_index][triangle_ptr] < grid[row_index][triangle_ptr + 1]:
            triangle_ptr += 1
        greatest_path_sum += grid[row_index][triangle_ptr]
        row_index += 1
    return greatest_path_sum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
    def rec_search_helper(grid, row, col):
        if row == len(grid) - 1:
            if col == row:
                return grid[row][col]
            return max(grid[row][col], grid[row][col + 1])
        else:
            return grid[row][col] + max(
                rec_search_helper(grid, row + 1, col),
                rec_search_helper(grid, row + 1, col + 1)
            )
    return rec_search_helper(grid, 0, 0)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    triangle = [[0 for num in row] for row in grid]
    for i in range(len(triangle) - 1, -1, -1):
        for j in range(len(triangle[i])):
            if i == len(triangle) - 1:
                triangle[i][j] = grid[i][j]
                if j == len(triangle) - 2:
                    triangle[i][j + 1] = grid[i][j + 1]
            else:
                triangle[i][j] = grid[i][j] + max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    in_file = open("./triangle.txt", "r")
    num_rows = int(in_file.readline().strip())
    return [[int(num) for num in in_file.readline().strip().split(" ")] for i in range(num_rows)]

# creates and returns a right triangle given size (with random integers from 1 to size ** 2)
def create_triangle(size):
    triangle = []
    for i in range(1, size):
        triangle.append([random.randint(1, size ** 2) for j in range(i)])
    return(triangle)

def main ():
    # read triangular grid from file
    triangle_grid = read_file()
    triangle_grid = create_triangle(20)

    ti = time.time()
    # output greatest path from exhaustive search
    print(f"The greatest path sum through exhaustive search is {exhaustive_search(triangle_grid)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search
    print(f"The time taken for exhaustive search is {del_t} seconds.\n")

    ti = time.time()
    # output greates path from greedy approach
    print(f"The greatest path sum through greedy search is {greedy(triangle_grid)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach
    print(f"The time taken for greedy search is {del_t} seconds.\n")

    ti = time.time()
    # output greates path from divide-and-conquer approach
    print(f"The greatest path sum through recursive search is {rec_search(triangle_grid)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print(f"The time taken for recursive search is {del_t} seconds.\n")

    ti = time.time()
    # output greates path from dynamic programming 
    print(f"The greatest path sum through dynamic programming is {dynamic_prog(triangle_grid)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using dynamic programming
    print(f"The time taken for dynamic programming is {del_t} seconds.")

if __name__ == "__main__":
    main()