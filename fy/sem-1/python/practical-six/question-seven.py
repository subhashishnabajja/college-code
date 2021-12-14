#WAP to find prime upto n.
# F093 / Subhashish Nabajja

def checkPrime(num):
    i = 2 
    while i < num:
        if num % i == 0:
            return False

        i += 1

    return True
    

def main():
    n = int(input("Enter a number: "))
    i = 2

    while i <= n:
        isPrime = checkPrime(i)

        if      isPrime: print(i)
        
        i += 1

if __name__ == "__main__":
    main()
