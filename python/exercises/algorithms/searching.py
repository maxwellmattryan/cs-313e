# SORTING ALGORITHMS

# Sequential Search -
# iterates through entire list until it finds the element
# returns -1 if not found
def sequentialSearch(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return(i)
    return(-1)

# Binary Search - 
# in a sorted list, if the target is lower than the median value
# search the left side, and vice versa. Repeat until found
# return -1 if not found
def binarySearch(arr, target):
    lo = 0
    hi = len(arr) - 1
    while(lo <= hi):
        mid = (lo + hi) // 2
        if(arr[mid] == target):
            return(mid)
        elif(arr[mid] > target):
            hi = mid - 1
        else:
            lo = mid + 1
    return(-1)

# PRINT METHOD FOR TIME 
# displays in ms if under 1 second, otherwise in s
def printTime(myTime):
    myTime = abs(myTime)
    if(myTime < 1):
        print("Time = ", "%.3f" % (myTime * 1000), "ms\n")
    else:
        print("Time = ", "%.3f" % myTime, "s\n\n")

# PRINT METHOD FOR ALGORITHMS
def printAlg(method, name, arr, target):
    # PRINT ALGORITHM
    print(name, "\n")
    totalTime = time.time()
    result = method(arr, target)
    totalTime -= time.time()
    printTime(totalTime)
    print("Index of", target, "=", result, "\n\n")

# RANDOM FOR LIST CREATION
import random
import time
import algorithms.sorting as sorting

def main():
    # N = SIZE OF ARRAY
    n = 1_000_000
    # CREATE RANDOM LIST OF N SIZE
    myList = [random.randint(-n, n) for i in range(n)]
    target = myList[len(myList) // 2]
    sorting.quickSort(myList, 0, len(myList) - 1)

    # SEQUENTIAL SEARCH
    printAlg(sequentialSearch, "Sequential Search", myList, target)
    # BINARY SEARCH
    printAlg(binarySearch, "Binary Search", myList, target)

main()