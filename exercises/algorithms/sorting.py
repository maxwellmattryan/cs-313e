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
def mergeSort(arr, *argv):
    if(len(arr) > 1):
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while(i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1
        while(j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1

# Quick Sort -
# description ...
def quickSort(arr, lo, hi):
    if(lo < hi):
        pivot = partition(arr, lo, hi)
        quickSort(arr, lo, pivot - 1)
        quickSort(arr, pivot + 1, hi)

def partition(arr, lo, hi):
    m = lo - 1
    pivot = arr[hi]
    for j in range(lo, hi):
        if(arr[j] < pivot):
            m += 1
            arr[m], arr[j] = arr[j], arr[m]
    arr[m + 1], arr[hi] = arr[hi], arr[m + 1]
    return(m + 1)


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
    method(tempList, 0, len(tempList) - 1)
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