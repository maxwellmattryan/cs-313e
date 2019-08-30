def makeSquare(size):
    return([[0 for i in range(size)] for j in range(size)])

def fillSquare(square):
    # count for filling square cells
    count = 1
    # row iterator
    rowIter = len(square[0]) - 1
    # column iterator
    colIter = len(square[0]) // 2
    print(str(rowIter) + " " + str(colIter))

    for i in range(len(square[0])):
        for j in range(len(square[0])):
            if(count > len(square[0]) ** 2):
                return(square)
            if(rowIter >= len(square[0]) and rowIter == colIter):
                square[rowIter - 2][colIter - 1] = count
                rowIter -= 1
            elif(rowIter == len(square[0])):
                square[0][colIter] = count
                rowIter = 1
                colIter += 1
            elif(colIter == len(square[0])):
                square[rowIter][0] = count
                colIter = 1
                rowIter += 1
            else:
                if(square[rowIter][colIter] == 0):
                    square[rowIter][colIter] = count
                else:
                    square[rowIter - 2][colIter - 1] = count
                    rowIter -= 2
                    colIter -= 1
                rowIter += 1
                colIter += 1
            count += 1
 
def printSquare(square):
    for i in range(len(square)):
        row = ""
        for j in range(len(square[i])):
            row += str(square[i][j]).center(3)
        print(row)

def main():
    size = eval(input("Enter a size: "))
    mySquare = makeSquare(size)
    printSquare(mySquare)
    square = fillSquare(mySquare)
    printSquare(mySquare)

main()