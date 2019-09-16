#  File: WordSearch.py

#  Description: Word Search | Assignment 04

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 09-13-2019

#  Date Last Modified: 09-15-2019

# Read file and return important variables / necessary data
def readFile():
    # absolute directory
    myFile = open(r"C:/Users/Matt/Documents/School/2019/Fall/cs-313e/assignments/4-word-search/hidden.txt", "r")
    # myFile = open("hidden.txt", "r")

    # Parse through the file, scraping important information
    # number of lines
    m = 0
    # number of characters per line
    n = 0
    # array of characters; THE word search
    wordSearch = []
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
        elif(lineIndex >= 2 and lineIndex <= m + 1):
            wordSearch.append([char for char in line.split(" ")])
        elif(lineIndex >= m + 4):
            words.append(line)
        lineIndex += 1
    print(m, n, wordSearch, words)
    return(m, n, wordSearch, words)
    myFile.close()

# Convert a list of chars to a string
def listToString(myList):
    myStr = ""
    for char in myList:
        myStr += char
    return(myStr)

# Parse the array of characters for the words
def searchForWord(wordSearch, word):
    while(True):
        # Loop through columns, check every column for word
        for j in range(len(wordSearch[0])):
            columnChars = [wordSearch[i][j] for i in range(len(wordSearch))]
            if(word in listToString(columnChars)):
                return(( listToString(columnChars).find(word), j ))
            elif(word in listToString(columnChars)[::-1]):
                wordIndex = listToString(columnChars)[::-1].find(word)
                return(( len(columnChars) - listToString(columnChars)[::-1].find(word) - 1, j))
        
        # Loop through rows, check every row for word
        for i in range(len(wordSearch)):
            rowChars = [wordSearch[i][j] for j in range(len(wordSearch[i]))]
            if(word in listToString(rowChars)):
                return(( i, listToString(rowChars).find(word) ))
            elif(word in listToString(rowChars)[::-1]):
                return(( i, len(rowChars) - listToString(rowChars)[::-1].find(word) - 1 ))

        # check rows (and reverse)
        # check diagonals (and reverse)
        break
    return((-1, -1))

# Checks a column for a word, returns a 
def checkColumn(columnString, word):
    print(columnString)
    print(word)
    print(word in columnString)
    print()

# Checks a row for a word, returns a string
def checkRow(rowString, word):
    print()

# Checks a diagonal for a word, returns a string
def checkDiagonal(diagonalString, word):  
    print()

def main():
    numberOfRows, numberOfColumns, wordSearch, words = readFile()
    for word in words:
        index = searchForWord(wordSearch, word)
        # add one for proper row / column numbering 
        print(word.ljust(16) + str(index[0] + 1).rjust(4) + str(index[1] + 1).rjust(4))

main()