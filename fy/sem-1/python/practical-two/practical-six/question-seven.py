def printPrime(end):
   

    for num in range(2,end +1):
        i = 2
        isPrime = True
        while i < num:
            if num % i == 0:
                isPrime = False
             
                break
            i+=1
               
        if isPrime: print(num)




printPrime(100)
