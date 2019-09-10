#  File: BabyNames.py 

#  Description: Assignment 03

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-10-2019

#  Date Last Modified: 09-10-2019

# TODO
# add try-except-finally for user command input

# read names from file, return stored data in dictionary
def getNames():
    names = {}
    namesFile = open(r"C:\Users\Matt\Documents\School\2019\Fall\cs-313e\assignments\baby-names-03\names.txt", "r")
    # namesFile = open("names.txt", "r")
    for line in namesFile:
        line = line.strip()
        lineItems = line.split(" ")
        decadeData = []
        for i in range(1, len(lineItems)):
            if(lineItems[i] == "0"):
                lineItems[i] = "1001"
            decadeData.append(int(lineItems[i]))
        names[lineItems[0]] = decadeData
    namesFile.close()
    return(names)

# searches for a name, returns true if in dictionary, false otherwise
def searchName(names):
    name = input("Enter a name to search for: ")
    print()
    namesHasName = name in names
    if(namesHasName):
        print("\"" + name + "\" was found\n")
    else:
        print("\"" + name + "\" was not found\n")
    return(namesHasName)

# display data for one name
def findName(names):
    name = input("Enter a name to find: ")
    print()

    # in case name is not within names
    while(name not in names):
        print("\"" + name + "\" was not found\n")
        name = input("Enter another name to find: ")
        print()

    print("Name".ljust(len(name) + 2) + "1900s".ljust(7) + "1910s".ljust(7) + "1920s".ljust(7) + "1930s".ljust(7) + "1940s".ljust(7) + "1950s".ljust(7) + "1960s".ljust(7) + "1970s".ljust(7) + "1980s".ljust(7) + "1990s".ljust(7) + "2000s".ljust(7))
    lineString = ""
    for i in range(len(names[name])):
        lineString += str(names[name][i]).ljust(7)
    print(name + "  " + lineString + "\n")

def main():
    names = getNames()

    # program loop, exits when user specifies to quit
    while(True):
        print(
            "Please pick an option below and enter its corresponding number:\n"
            "\n"
            "1: Search for a name\n"
            "2: Find data for a name\n"
            "3: Display all names of a given decade\n"
            "4: Display all names of all decades\n"
            "5: Display increasingly popular names for each decade\n"
            "6: Display decreasingly popular names for each decade\n"
            "7: Quit the program\n"
            )
        command = eval(input())
        print()

        # COMMAND ROUTING
        # NAME SEARCH
        if(command == 1):
            searchName(names)
        elif(command == 2):
            findName(names)
        elif(command == 7):
            break
    return

main()