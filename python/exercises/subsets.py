# dependencies
import random

# return a list of subsets of a given list
def subsets(my_list):
    # init variable for storing list of subsets, returned at end
    subset_list = []

    # helper method with extra parameters 
    def h_subsets(index, subset):
        if index < len(my_list):
            h_subsets(index + 1, list(subset))
            subset.append(my_list[index])
            h_subsets(index + 1, subset)
        else:
            subset_list.append(subset)

    # return subset list after calling method
    h_subsets(0, [])
    return subset_list

# returns sum of series from lo (default = 1) and hi
def sum_series(lo, hi):
    # helper method with extra 'result' parameter
    def h_sum_series(lo, hi, result):
        if hi < lo:
            return result
        return h_sum_series(lo, hi - 1, result + hi)
    return h_sum_series(lo, hi, 0)

def main():

    # get number from user
    high_num = eval(input("Enter a high number: "))
    print(f"sum_series({high_num}) => {sum_series(1, high_num):,}\n")

    # init random list of stuff
    size = eval(input("Enter any size: "))
    print()

    # init random list from characters 'a' to 'z' 
    rand_list = sorted([chr(random.randint(ord('a'), ord('z'))) for i in range(size)])
    
    print(f"subsets({rand_list}) => ...")

    # get list of subsets
    subset_list = sorted(subsets(rand_list))

    # print every subset in ^ list
    #[print(subset) for subset in subset_list]

    # print the total amount
    print(f"\nThere are {len(subset_list):,} total subsets for a list of size {size}\n")

    # test all sizes up to original size
    for size in range(size + 1):
        rand_list = sorted([chr(random.randint(ord('a'), ord('z'))) for i in range(size)])
        subset_list = sorted(subsets(rand_list))
        print(f"{size} : {len(subset_list):,}")

main()