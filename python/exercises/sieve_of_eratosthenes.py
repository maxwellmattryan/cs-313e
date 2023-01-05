import math
import time

# given the boolean array and a starting prime, sieve all numbers that are multiples of that prime
def sieve(bool_arr, prime):
    p_multiple = prime * 2
    while(p_multiple < bool_arr[-1]):
        while(p_multiple % 2 == 0):
            p_multiple += prime
        if(p_multiple > bool_arr[-1]):
            break
        bool_arr[p_multiple // 2] = 0
        p_multiple += prime


# given the boolean array and a current prime number location, find the next prime number in the array (the next number that is still valid)
def get_next_prime(bool_arr, prime):
    next_prime = bool_arr[prime // 2 + 1]
    while(next_prime < len(bool_arr) and bool_arr[next_prime] == 0):
        next_prime += 1
    return(next_prime)

# given the boolean array, return a new list containing all valid elements in the boolean array
def get_primes(bool_arr):
    return([bool_arr[i] for i in range(len(bool_arr)) if(bool_arr[i] != 0)])

def main():
    # get input from user, and add one for offsetting 0-based index 
    sieve_max = eval(input("Enter a max for the Seive of Eratosthenes: ")) + 1
    
    # generate boolean array of primes, init to all 1s except for 0 and 1
    bool_arr = [i for i in range(sieve_max) if ((i % 2 != 0 and i > 2) or i == 2)]
    
    # starting with prime = 3, iterate through boolean array and flag multiples of that prime
    prime = 3
    elapsed_time = time.time()
    while(prime <= math.sqrt(sieve_max)):
        if(prime * prime > sieve_max):
            break
        sieve(bool_arr, prime)
        prime = get_next_prime(bool_arr, prime)
    elapsed_time = time.time() - elapsed_time
    
    # get all primes from boolean array
    primes = get_primes(bool_arr)

    # output statements
    print(f"sieve_of_eratosthenes({sieve_max - 1:,}) => {primes[0]}, ..., {primes[-3]}, {primes[-2]}, {primes[-1]}\n")
    print(f"Total elapsed time = {elapsed_time:.03f} seconds")

main()