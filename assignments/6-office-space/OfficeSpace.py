#  File: OfficeSpace.py

#  Description: Assignment 06 | Office Space

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-23-2019

#  Date Last Modified: 09-23-2019

# read data from file
def readFile():
    myFile = open("office.txt", "r")
    dataSet = []
    data = []
    lines = [line.strip() for line in myFile]
    i = 0
    while(i < len(lines)):
        if(i == 0):
            points = lines[i].split(" ")
            data.append((int(points[0]), int(points[1])))
            i += 1
        elif(i == 1):
            for j in range(2, 2 + int(lines[i])):
                employee = lines[j].split(" ")
                name = employee[0]
                lowerLeftPoint = [int(employee[1]), int(employee[2])]
                upperRightPoint = [int(employee[3]), int(employee[4])]
                data.append([name, lowerLeftPoint, upperRightPoint])
                i += 1
            dataSet.append(data)
            data = []
            lines = lines[i + 1:]
            i = 0
    print()
    myFile.close()
    return(dataSet)

# create and populate office grid with requests
def makeOfficeGrid(myData):
    # fill grid with zeros
    grid = [[0 for j in range(myData[0][0])] for i in range(myData[0][1])]

    # populate grid from employee requests
    colOffset = len(grid) # used for subtracting the y coordinates from grid length to get correct grid coordinates
    for employee in myData[1:]:
        for i in range(colOffset - employee[2][1], colOffset - employee[1][1]):
            for j in range(employee[1][0], employee[2][0]):
                grid[i][j] += 1
    return(grid)

# return integer of amount of contested space
def processRequests(grid, employees):
    unallocatedSpace = 0
    contestedSpace = 0
    for row in grid:
        for column in row:
            if(column == 0):
                unallocatedSpace += 1
            elif(column >= 2):
                contestedSpace += 1
    colOffset = len(grid)
    for employee in employees:
        employeeSpace = 0
        for i in range(colOffset - employee[2][1], colOffset - employee[1][1]):
            for j in range(employee[1][0], employee[2][0]):
                if(grid[i][j] == 1):
                    employeeSpace += 1
        employee.append(employeeSpace)

    return(unallocatedSpace, contestedSpace, employees)

# print data according to format
def printData(myData, unallocatedSpace, contestedSpace):
    totalArea = myData[0][0] * myData[0][1]
    # total area of office space (x times y)
    print("Total " + str(totalArea))
    # unallocated area of office space (total minus area of squares)
    print("Unallocated " + str(unallocatedSpace))
    # contested area of office space (find total area of rectangular overlap)
    print("Contested " + str(contestedSpace))
    # each employee with guaranteed space (original request minus contested) * same order as input
    [print(employee[0] + " " + str(employee[3])) for employee in myData[1:]]
    print()

# tool to print and check the grid
def printGrid(grid):
    print("Dimensions: " + str(len(grid[0])) + " x " + str(len(grid)))
    [print(unit) for unit in grid]
    print()

def main():
    myDataSet = readFile()
    for myData in myDataSet:
        officeGrid = makeOfficeGrid(myData)
        unallocatedSpace, contestedSpace, myData[1:] = processRequests(officeGrid, myData[1:])
        printData(myData, unallocatedSpace, contestedSpace)

main()