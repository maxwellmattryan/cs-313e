#  File: BabyNames.py 

#  Description: Assignment 03

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-10-2019

#  Date Last Modified: 09-13-2019

# read names from file, return stored data in dictionary
def getNames():
    names = {}
    try:
        namesFile = open("names.txt", "r")
    except FileNotFoundError:
        print("The file was not found. Please try again.\n")
    for line in namesFile:
        line = line.strip()
        lineItems = line.split(" ")
        decadeData = [int(lineItems[i]) for i in range(1, len(lineItems))]
        names[lineItems[0]] = decadeData
    namesFile.close()
    return(names)

# 1: searches for a name, returns true if in dictionary, false otherwise
def searchName(names):
    name = input("Enter a name: ").capitalize()
    print()

    # in case name is not within names
    if(name not in names):
        print(name + " does not appear in any decade.\n")
        return(False)

    ## FIND A WAY TO GET HIGHEST RANKS (CAN BE THE SAME)
    minRank = min(names[name])
    indeces = []
    for i in range(len(names[name])):
        if(names[name][i] == minRank):
            indeces.append(i)

    print("The matches with their highest ranking decade(s) are: ")
    lineString = name + " "
    for i in indeces:
        if(i == 10):
            lineString += "2000"
        else:
            lineString += str(19) + str(i) + str(0) + " "
    print(lineString + "\n")

# 2: display data for one name
def findName(names):
    name = input("Enter a name: ").capitalize()
    print()
    
    # print data for name
    print(name + ": " + " ".join(str(num) for num in names[name]))
    for i in range(len(names[name])):
        if(i == 10):
            print("2000: " + str(names[name][i]))
        else:
            print(str(19) + str(i) + str(0) + ": " + str(names[name][i]))
    print()

# 3: display all names of a given decade in order of rank
def displayNamesOfDecade(names):
    decade = input("Enter decade: ")
    if(decade[0] == "2"):
        decadeIndex = 10
    else:
        decadeIndex = int(decade[2])

    reducedNames = []
    for name in names:
        if(names[name][decadeIndex] != 0):
            reducedNames.append([names[name][decadeIndex], name])
    reducedNames.sort()
    
    print("The names are in order of rank: ")
    for name in reducedNames:
        print(name[1] + ": " + str(name[0]))
    print()

# 4: display all names of all decades
def displayNamesOfAllDecades(names):
    namesOfAllDecades = []
    for name in names:
        for i in range(len(names[name])):
            if(names[name][i] == 0):
                break
            elif(i == len(names[name]) - 1):
                namesOfAllDecades.append(name)
    
    print(str(len(namesOfAllDecades)) + " names appear in every decade. The names are:")
    for name in namesOfAllDecades:
        print(name)
    print()

# 5: display all names that are more popular in every decade
def displayNamesOfIncreasingPopularity(names):
    morePopularNames = []
    for name in names:
        previousRank = names[name][0]
        for i in range(1, len(names[name])):
            currentRank = names[name][i]
            if(currentRank >= previousRank or names[name][i] == 0):
                break
            elif(i == len(names[name]) - 1):
                morePopularNames.append(name)
            previousRank = currentRank

    print(str(len(morePopularNames)) + " names are more popular every decade.")
    for name in morePopularNames:
        print(name)
    print()

# 6: display all names that are less popular in every decade
def displayNamesOfDecreasingPopularity(names):
    lessPopularNames = []
    for name in names:
        previousRank = names[name][0]
        for i in range(1, len(names[name])):
            currentRank = names[name][i]
            # if(currentRank == 0 and i != len(names[name]) - 1):
            #     break
            if((currentRank <= previousRank and i != len(names[name]) - 1) or (currentRank == 0 and i != len(names[name]) - 1)):
                break
            elif(i == len(names[name]) - 1 and (names[name][i] == 0 or currentRank > previousRank)):
                lessPopularNames.append(name)
            previousRank = currentRank

    print(str(len(lessPopularNames)) + " names are less popular every decade.")
    for name in lessPopularNames:
        print(name)
    print()

def main():
    names = getNames()

    # program loop, exits when user specifies to quit
    while(True):
        print(
            "Options:\n"
            "Enter 1 to search for names.\n"
            "Enter 2 to display data for one name.\n"
            "Enter 3 to display all names that appear in only one decade.\n"
            "Enter 4 to display all names that appear in all decades.\n"
            "Enter 5 to display all names that are more popular in every decade.\n"
            "Enter 6 to display all names that are less popular in every decade.\n"
            "Enter 7 to quit.\n"
            )

        # COMMAND ROUTING / ERROR HANDLING
        try:
            command = eval(input("Enter choice: "))
            if(command == 1):
                searchName(names)
            elif(command == 2):
                findName(names)
            elif(command == 3):
                displayNamesOfDecade(names)
            elif(command == 4):
                displayNamesOfAllDecades(names)
            elif(command == 5):
                displayNamesOfIncreasingPopularity(names)
            elif(command == 6):
                displayNamesOfDecreasingPopularity(names)
            elif(command == 7):
                print("\nGoodbye.")
                break
        except:
            print()
    return

main()