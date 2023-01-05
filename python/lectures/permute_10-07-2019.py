def permute(a, lo):
    hi = len(a)
    if(lo == hi):
        if(a[0] != "A" and a[1] != "B" and a[2] != "C" and a[3] != "D"):
            print(a)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute(a, lo + 1)
            a[lo], a[i] = a[i], a[lo]
def main():
    a = ["A", "B", "C", "D"]
    permute(a, 0)

main()