# SORTING ALGORITHMS

# Selection Sort -
# repeatedly finds lowest element within unsorted partition,
# then places it at the end of the sorted partition
def selectionSort(arr, *argv):
    n = len(arr)
    for i in range(n):
        minimum = arr[i]
        minIdx = i
        for j in range(i, n):
            if(arr[j] < minimum):
                minimum = arr[j]
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

# Bubble Sort - 
# swaps elements if they are in the wrong order while
# continually moving through the array
def bubbleSort(arr, *argv):
    sorted = False
    while(not sorted):
        swapped = False
        for i in range(len(arr) - 1):
            if(arr[i + 1] < arr[i]):
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                swapped = True
        if(not swapped):
            break

# Insertion Sort -
# insert an element in the proper index according to the 
# elements before it
def insertionSort(arr, *argv):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while(j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort -
# description ...
def mergeSort(arr, left, right):
    if(left < right):
        print("FIXME: Start merge sort !")

# Quick Sort -
# description ...
def quickSort(arr, lo, hi):
    print("FIXME: Start quick sort !")
    if(lo >= hi):
        print()

# PRINT METHOD FOR TIME 
# displays in ms if under 1 second, otherwise in s
def printTime(myTime):
    myTime = abs(myTime)
    if(myTime < 1):
        print("Time = ", "%.3f" % (myTime * 1000), "ms\n")
    else:
        print("Time = ", "%.3f" % myTime, "s\n\n")

# PRINT METHOD FOR ALGORITHMS
def printAlg(method, name, arr):
    tempList = arr[:]
    # PRINT ALGORITHM
    print(name, "\n\nUnsorted:\n", tempList, "\n")
    totalTime = time.time()
    method(tempList, 0, len(tempList))
    totalTime -= time.time()
    print("Sorted:\n", tempList, "\n")
    printTime(totalTime)

# RANDOM FOR LIST CREATION
import random
import time

def main():
    # N = SIZE OF ARRAY
    n = 250
    # CREATE RANDOM LIST OF N SIZE
    myList = [random.randint(-n, n) for i in range(n)]

    # SELECTION SORT
    printAlg(selectionSort, "Selection Sort", myList)
    # BUBBLE SORT
    printAlg(bubbleSort, "Bubble Sort", myList)
    # INSERTION SORT
    printAlg(insertionSort, "Insertion Sort", myList)
    # MERGE SORT
    printAlg(mergeSort, "Merge Sort", myList)
    # QUICK SORT
    printAlg(quickSort, "Quick Sort", myList)

main()