#  File: Boxes.py

#  Description: Assignment 13 | Nesting Boxes

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10-17-2019

#  Date Last Modified: 10-17-2019

# read data from file, return list of boxes
def getBoxes():
    myFile = open("./boxes.txt", "r")
    numBoxes = int(myFile.readline().strip())
    boxes = []
    for i in range(numBoxes):
        box = [int(dim) for dim in myFile.readline().strip().split(" ")]
        box.sort()
        boxes.append(box)
    boxes.sort()
    myFile.close()
    return(boxes)

# returns boolean of if a box fits in another
def canNest(box1, box2):
    return(box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

# returns true if elements in list can nest
def canNestAll(subset):
    for i in range(0, len(subset) - 1):
        if(not canNest(subset[i], subset[i + 1])):
            return(False)
    return(True)

# prints all subsets of a list
def subsets(a, b, lo, nestSubs):
    hi = len(a)
    if(lo == hi):
        if(canNestAll(b)):
            nestSubs.append(b)
        return
    else:
        c = b[:]
        b.append(a[lo])
        subsets(a, b, lo + 1, nestSubs)
        subsets(a, c, lo + 1, nestSubs)

def main():
    boxes = getBoxes()

    nestSubs = []
    subsets(boxes, [], 0, nestSubs)

    maxSize = max([len(subset) for subset in nestSubs])

    print(f"Largest Subset of Nesting Boxes")
    for subset in nestSubs:
        if(len(subset) == maxSize):
            [print(box) for box in subset]
            print()
    
    if(maxSize < 2):
        print("No Nesting Boxes")

main()