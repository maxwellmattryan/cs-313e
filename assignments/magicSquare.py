def makeSquare(size):
    return([[0 for i in range(size)] for j in range(size)])

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

main()