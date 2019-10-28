#  File: Reducible.py

#  Description: Assignment 15 | Reducible Words 

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 10-27-2019

#  Date Last Modified: 10-27-2019

# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
    print("FIXME: Define find_word()")

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
    print("FIXME: Define get_longest_words()")

# goes through input file and returns the word list
def get_word_list():
    myFile = open("words.txt", "r")
    words = [line.strip() for line in myFile]
    myFile.close()
    return(words)

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
    hashIndex = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hashIndex = (hashIndex * 26 + letter) % size
    return(hashIndex)

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
    # create initial index and test until there is a valid index
    index1 = hash_word(s, len(hash_table))
    if(hash_table[index1] != ""):
        index2 = 13 - (index1 % 13)
        i = 0
        while(True):
            newindex = (index1 + i * index2) % len(hash_table)
            if(hash_table[newindex] == ""):
                hash_table[newindex] = s
                break
            i += 1
    else:
        hash_table[index1]

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime (n):
    if(n == 1):
        return(False)
    limit = int(n ** 0.5) + 1
    div = 2
    while(div < limit):
        if(n % div == 0):
            return(False)
        div += 1
    return(True)

# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible (s, hash_table, hash_memo):
    print("FIXME: Define is_reducible()")

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size (s, const):
    return(-1)

def main():
    # read data in as the list of curated words
    words = get_word_list()
    [print(word) for word in words]

    # determine a prime number that is greater than twice the length of the words
    primeNum = len(words) * 2 + 1
    while(not is_prime(primeNum)):
        primeNum += 1

    # create an empty hash list with the prime number of blank strings
    h_words = ["" for i in range(primeNum)]

    # hash each word in words into h_words for collisions using double hashing 
    for word in words:
        insert_word(word, h_words)

    # create an empty hash_memo

    # populate the hash_memo with M blank strings

    # create and empty list reducible_words

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words

    # find words of the maximum length in reducible_words

    # print the words of maximum length in alphabetical order
    # one word per line

# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()