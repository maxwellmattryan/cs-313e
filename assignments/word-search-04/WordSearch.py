#  File: WordSearch.py

#  Description: Word Search | Assignment 04

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 09-13-2019

#  Date Last Modified: 09-13-2019

# Read file and return important variables / necessary data
def readFile():
    # absolute directory
    myFile = open(r"C:/Users/Matt/Documents/School/2019/Fall/cs-313e/assignments/word-search-04/hidden.txt", "r")
    ### myFile = open("hidden.txt", "r")

    # Parse through the file, scraping important information
    # number of lines
    m = 0
    # number of characters per line
    n = 0
    # list of words that are in the word search 
    words = []
    lineIndex = 0
    for line in myFile:
        line = line.strip()
        if(lineIndex == 0):
            # number of lines
            m = int(line.split(" ")[0])
            # number of characters per line
            n = int(line.split(" ")[1])
        elif(lineIndex >= m + 4):
            words.append(line)
        lineIndex += 1
    print(m, n, words)
    return(m, n, words)
    myFile.close()

def main():
    rows, columns, words = readFile()

main()