#WAP to find the product of numbers from 1 to n. (Factorial)
# F093 / Subhashish Nabajja

def factorial():
    n = int(input("Enter a number: "))

    i = 1
    fact = i
   

    while i <= n :
        fact *= i
        i += 1

    print(fact)

factorial()
    
