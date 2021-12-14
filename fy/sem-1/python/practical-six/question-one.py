#WAP to print numbers from 1 to the limit entered by the user, using a while loop.
# F093 / Subhashish


def printNumbers():
    limit = int(input("Enter the ending point: "))
    i = 1

    while i <= limit:
        print(i)
        i += 1

printNumbers()
