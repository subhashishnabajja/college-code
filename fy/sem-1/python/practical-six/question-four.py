#WAP to find the sum of numbers from 1 to n.
# F093 / Subhashish Nabajja

def printSum():
    n = int(input("Enter a number: "))
    sum = 0
    i = 0

    while i <= n :
        sum += i
        i += 1

    print(sum)

printSum()
    
