#WAP to print even numbers from start to the limit entered by the user, using a while loop.
# F093 / Subhashish Nabajja

def printEvenNumbers():
    start = int(input("Enter the starting point: "))
    limit = int(input("Enter the ending point: "))

    i = start

    while i <= limit:
        if i % 2 == 0 : print(i)
        i += 1


printEvenNumbers()
