def cut_rod(prices, rod_size):
    r = s = [0 for i in range(rod_size + 1)]
    for j in range(1, rod_size + 1):
        max_price = -1
        for k in range(1, j + 1):
            new_price = 0
            if(k < len(prices)):
                new_price = prices[k] + r[j - k]
            else:
                new_price = r[j - k]
            if(new_price > max_price):
                max_price = new_price
                s[j] = k
        r[j] = max_price
    print(r)
    print(s)
    return r,s

def main():
    # define the price per length of a rod
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]

    # prompt the user to enter the size of the rod to be cut
    rod_size = int(input("Enter the rod's size: "))
    print()

    # get the optimal price for cutting a rod of size rod_size
    r, s = cut_rod(prices, rod_size)

    # print the optimal solution
    print(f"Optimal price = {r[rod_size]}")

    # print the cuts of the rod
    while(rod_size > 0):
        print(s[rod_size])
        rod_size -= s[rod_size]

main()