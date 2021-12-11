def printEvenNumbers():
    start = int(input("Enter the starting number:"))
    end = int(input("Enter the ending number:"))

    i = start

    while i <= end:
        if i % 2 == 0: print(i)
        i+=1

printEvenNumbers()
