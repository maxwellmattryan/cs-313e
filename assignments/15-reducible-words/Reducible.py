#  File: Reducible.py

#  Description: Assignment 15 | Reducible Words 

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205 

#  Date Created: 10-24-2019

#  Date Last Modified: 10-24-2019

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
    print("FIXME: Define get_word_list()")
    return(-1)
    # create an empty word_list
    # open the file words.txt
    # read words from words.txt and append to word_list
    # close file words.txt

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
    print("FIXME: Define: hash_word()")

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
    print("FIXME: Define: insert_word()")

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime (n):
    print("FIXME: Define: is_prime()")

# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible (s, hash_table, hash_memo):
    print("FIXME: Define is_reducible()")

def main():
    word_list = get_word_list()
    print(word_list)
    # find length of word_list

    # determine prime number N that is greater than twice
    # the length of the word_list

    # create and empty hash_list

    # populate the hash_list with N blank strings

    # hash each word in word_list into hash_list
    # for collisions use double hashing 

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