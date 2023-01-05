# Read file and return important variables / necessary data
def readFile():
    myFile = open("hidden.txt", "r")

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
    return(wordSearch, words)
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

        # Loop through left => right diagonals, check every diagonal for word
        i = len(wordSearch) - 1
        j = 0
        for k in range(len(wordSearch) + len(wordSearch[0]) - 1): # k = amount of diagonals
            row = i
            col = j
            diagonalChars = []
            # diagonal starting from 0, 0
            if(i == 0 and j == 0):
                diagonalChars = [wordSearch[iter][iter] for iter in range(len(wordSearch))]
                j += 1
                if(word in listToString(diagonalChars)):
                    return(( listToString(diagonalChars).find(word), listToString(diagonalChars).find(word) ))
                elif(word in listToString(diagonalChars)[::-1]):
                    return(( len(listToString(diagonalChars)) - listToString(diagonalChars)[::-1].find(word) - 1, len(listToString(diagonalChars)) - listToString(diagonalChars)[::-1].find(word) - 1 ))
            # other diagonals
            elif((i == 0 and j > 0) or (i > 0 and j == 0)):
                while(row < len(wordSearch) and col < len(wordSearch[0])):
                    diagonalChars.append(wordSearch[row][col])
                    row += 1
                    col += 1
                if(word in listToString(diagonalChars)):
                    return(( i + listToString(diagonalChars).find(word), j + listToString(diagonalChars).find(word) ))
                elif(word in listToString(diagonalChars)[::-1]):
                    return(( i + listToString(diagonalChars).find(word[::-1]) + len(word) - 1, j + listToString(diagonalChars).find(word[::-1]) + len(word) - 1 ))
                
                # index maintenance
                if(i == 0 and j > 0):
                    j += 1
                elif(i > 0 and j == 0):
                    i -= 1   

        # Loop through right => left diagonals, check every diagonal for word
        i = len(wordSearch) - 1
        j = len(wordSearch) - 1
        for k in range(len(wordSearch) + len(wordSearch[0]) - 1): # k = amount of diagonals
            row = i
            col = j
            diagonalChars = []
            # diagonal starting from 0, 0
            if(i == 0 and j == len(wordSearch) - 1):
                diagonalChars = [wordSearch[len(wordSearch) - iter - 1][iter] for iter in range(len(wordSearch) - 1, -1, -1)]
                j -= 1
                if(word in listToString(diagonalChars)):
                    return(( i + listToString(diagonalChars).find(word), j - listToString(diagonalChars).find(word) ))
                elif(word in listToString(diagonalChars)[::-1]):
                    return(( len(listToString(diagonalChars)) - listToString(diagonalChars)[::-1].find(word) - 1, listToString(diagonalChars)[::-1].find(word) ))
            # other diagonals
            elif((i == 0 and j < len(wordSearch) - 1) or (i > 0 and j == len(wordSearch) - 1)):
                while(row < len(wordSearch) and col < len(wordSearch[0])):
                    diagonalChars.append(wordSearch[row][col])
                    row += 1
                    col -= 1
                if(word in listToString(diagonalChars)):
                    return(( i + listToString(diagonalChars).find(word), j - listToString(diagonalChars).find(word) ))
                elif(word in listToString(diagonalChars)[::-1]):
                    return(( j - listToString(diagonalChars)[::-1].find(word), i + listToString(diagonalChars)[::-1].find(word) ))

                # index maintenance
                if(i == 0 and j < len(wordSearch) - 1):
                    j -= 1
                elif(i > 0 and j == len(wordSearch) - 1):
                    i -= 1

        break
    return((-1, -1))

# Write to an output file
def writeToFile(myString):
    myFile = open("found.txt", "a")
    myFile.write(myString)
    myFile.close()

def main():
    wordSearch, words = readFile()
    for word in words:
        index = searchForWord(wordSearch, word)
        writeToFile(word.ljust(max([len(myWord) for myWord in words])) + str(index[0] + 1).rjust(4) + str(index[1] + 1).rjust(4) + "\n")

main()