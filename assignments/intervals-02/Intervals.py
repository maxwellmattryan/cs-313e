#  File: Intervals.py

#  Description: Assignment 02 

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-04-2019

#  Date Last Modified: 09-09-2019

# READ FILE, RETURN LIST OF TUPLES
def getTuples():
    # myFile = open("C:/Users/Matt/Documents/School/2019/Fall/cs-313e/assignments/intervals-02/backup.txt", "r")
    # only an absolute path worked on my machine, but here is the proper way
    myFile = open("intervals.txt", "r")
    
    myTuples = []
    for line in myFile:
        line = line.strip()
        nums = line.split(" ")
        myTuples.append((int(nums[0]), int(nums[1])))
    myFile.close()

    sortIntervals(myTuples)
    return(myTuples)

# SORT LIST OF TUPLES
def sortIntervals(intervals):
    intervals.sort()

# CHECK FOR OVERLAPPING INTERVALS AND COLLAPSE
def collapse(intervals):
    collapsedIntervals = intervals
    i = 0
    while(i + 1 <= len(collapsedIntervals) - 1):
        if(collapsedIntervals[i][1] >= collapsedIntervals[i + 1][0]):
            if(collapsedIntervals[i][1] > collapsedIntervals[i + 1][1]):
                collapsedIntervals[i + 1] = (collapsedIntervals[i][0], collapsedIntervals[i][1])
            else:
                collapsedIntervals[i + 1] = (collapsedIntervals[i][0], collapsedIntervals[i + 1][1])
            collapsedIntervals.remove(collapsedIntervals[i])
        else:
            i += 1
    return(collapsedIntervals)

# PRINT LIST OF TUPLES
def printTuples(intervals):
    print("Non-intersecting Intervals:")
    for i in range(len(intervals)):
        print(intervals[i])
    print()

# GET SIZES OF COLLAPSED INTERVALS, RETURNS LIST WITH LISTS OF SIZE AND THE TUPLE (FOR PRINTING)
def getSizes(intervals):
    sizes = []
    for interval in intervals:
        distance = interval[1] - interval[0]
        sizes.append([distance, interval])
    sizes.sort()
    return(sizes)

# PRINT TUPLES IN ORDER OF SIZE
def printSizes(sizes):
    print("Non-intersecting Intervals in order of size:")
    for size in sizes:
        print(size[1])

def main():
    myTuples = getTuples()
    myTuples = collapse(myTuples)
    printTuples(myTuples)
    mySizes = getSizes(myTuples)
    printSizes(mySizes)

main()