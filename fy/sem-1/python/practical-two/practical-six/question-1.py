def printEvenNumbers():
    limit = int(input("Enter a limit:"))
    i = 1
    while i <= limit:
        if i % 2 == 0: print(i)
        i+=1


printEvenNumbers()
