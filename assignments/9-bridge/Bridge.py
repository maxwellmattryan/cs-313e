#  File: Bridge.py 

#  Description: Assignment 09 | Bridge

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E
 
#  Unique Number: 50205 

#  Date Created: 09-30-2019

#  Date Last Modified: 10-01-2019

# read file in, return data set of test cases
def readFile():
    myFile = open("bridge.txt", "r")
    lines = [line.strip() for line in myFile]
    numCases = int(lines[0])
    lines = lines[2:]
    dataSet = []
    for i in range(numCases):
        dataItem = []
        for j in range(int(lines[0])):
            dataItem.append(int(lines[j + 1]))
        lines = lines[int(lines[0]) + 2:]
        dataItem.sort()
        dataSet.append(dataItem)
    myFile.close()
    return(dataSet)

# simple recursive function to find total lowest crossing time
def fastBridgeCross(people):
    # if there is one or two people, return highest time
    if(len(people) <= 2):
        return(people[len(people) - 1])
    # if there are three people, return the sum of all three
    elif(len(people) == 3):
        return(sum(people))
    # if there are >3 people, then compute movements for the slowest two people to get to the other side, then call function again without two slowest people
    else:
        return(fastBridgeCross(people[:-2]) + people[0] + (people[1] * 2) + people[-1])

def main():
    myDataSet = readFile()
    [print(fastBridgeCross(item), "\n") for item in myDataSet]

main()