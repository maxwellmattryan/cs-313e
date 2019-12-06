def permute(arr, lo, hi, permutations):
    if(lo == hi):
        print(arr)
        permutations.append(arr)
    else:
        for i in range(lo, hi):
            arr[lo], arr[i] = arr[i], arr[lo]
            permute(arr, lo + 1, hi, permutations)
            arr[lo], arr[i] = arr[i], arr[lo]

def main():
    size = 10
    myList = [i + 1 for i in range(size)]
    permutations = []
    permute(myList, 0, len(myList), permutations)
    print(f"\n{len(permutations)} total permutations")

main()