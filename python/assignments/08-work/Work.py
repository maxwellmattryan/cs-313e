#  File: Work.py 

#  Description: Assignment 08 | Work 'Till You Drop

#  Student Name:  Matthew Maxwell

#  Student UT EID:  mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-28-2019

#  Date Last Modified: 09-30-2019

import time

# read file from data
def readFile():
    myFile = open("work2.txt", "r")
    lines = [line.strip() for line in myFile][1:]
    myFile.close()
    return([(int(line.split(" ")[0]), int(line.split(" ")[1])) for line in lines])

# use binary search to find lowest amount of lines 
def findLowestLines(test):
    lo = 1
    hi = test[0]
    mid = (lo + hi) // 2
    k = test[1]
    while(lo != mid):
        if(sumSeries(mid, k) >= test[0]):
            hi = mid
        elif(sumSeries(mid, k) < test[0]):
            lo = mid
        mid = (lo + hi) // 2
    if(sumSeries(mid, k) < test[0]):
        return(mid + 1)
    return(mid)

# use sequential search to find lowest amount of lines
def sequentiallyFindLowestLines(test):
    for num in range(test[0]):
        if(sumSeries(num, test[1]) >= test[0]):
            return(num)
    return(-1)

# sum results while (v // k ** i) is greater than 0
def sumSeries(v, k):
    sum = v
    exp = 1
    while(k ** exp <= v):
        sum += v // (k ** exp)
        exp += 1
    return(sum)

def main():
    myTests = readFile()
    
    print("Binary Search: ")
    startTime = time.time()
    [print(findLowestLines(test)) for test in myTests]
    print("Total time: %.2f" % ((time.time() - startTime) * 1000), "milliseconds\n")

    print("\nSequential Search: ")
    startTime = time.time()
    [print(sequentiallyFindLowestLines(test)) for test in myTests]
    print("Total time: %.2f" % ((time.time() - startTime) * 1000), "milliseconds\n")

main()