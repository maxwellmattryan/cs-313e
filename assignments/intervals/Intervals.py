#  File: Intervals.py

#  Description: Assignment 02 

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-04-2019

#  Date Last Modified: 09-04-2019

# READ FILE, RETURN LIST OF TUPLES
def getTuples():
    # myFile = open("intervals.txt", "r")
    # myTuples = []
    # for line in myFile:
    #     line = line.strip()
    #     print(line)
    #     print(line.split(" "))
    # myFile.close()

    # FIX LATER, FOR NOW USING HARDCODED LIST OF TUPLES....
    myTuples = [
        (14, 17),
        (-8, -5),
        (26, 29),
        (-20, -15),
        (12, 15),
        (2, 3),
        (-10, -7),
        (25, 30),
        (2, 4),
        (-21, -16),
        (13, 18),
        (22, 27),
        (-6, -3),
        (3, 6),
        (-25, -14)
    ]

    moreTuples = [
        (-4, -2),
        (-3, 0),
        (0, 1),
        (2, 4)
    ]

    sortIntervals(myTuples)
    return(myTuples)

# SORT LIST OF TUPLES
def sortIntervals(intervals):
    intervals.sort()

# CHECK FOR OVERLAPPING INTERVALS AND COLLAPSE
def collapse(intervals):
    collapsedIntervals = []
    start = intervals[0][0]
    end = intervals[0][0]
    
    placeholder = start
    for i in range(len(intervals) - 1):
        for j in range(intervals[i][0], intervals[len(intervals) - 1][1]):
            placeholder += 1
            if(placeholder == intervals[i + 1][0]):
                i += 1
                continue
            elif(intervals[i][0] == intervals[i + 1][0]):
                i += 1
                placeholder = intervals[i][0]
                continue
            elif(placeholder == intervals[i][1]):
                end = placeholder
                collapsedIntervals.append((start, end))
                if(i + 1 == len(intervals) - 1): 
                    collapsedIntervals.append((intervals[i + 1][0], intervals[i + 1][1]))
                    return(collapsedIntervals)
                else:
                    start = intervals[i + 1][0]
                    placeholder = start
                i += 1
                continue
        break
    print(collapsedIntervals)



# PRINT LIST OF TUPLES

# EXTRA CREDIT: PRINT LIST OF TUPLES IN ORDER OF THEIR INTERVAL SIZE
# IF SIZE IS SAME, THEN PRINT BOTH IN ORDER ACCORDING TO THE TUPLE'S
# FIRST NUMBER


def main():
    myTuples = getTuples()
    myTuples = collapse(myTuples)

main()