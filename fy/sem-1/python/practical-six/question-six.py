#WAP to find fibonacci series upto n.
# F093 / Subhashish Nabajja

def fibonacci():
    n = int(input("Enter a number: "))

    i = 1
    t1 = 0
    t2  = 1
    t3 = 0
   

    while i <= n :
        print(t1)
        t3 = t2 + t1
        t1 = t2
        t2 = t3
        i += 1

 

fibonacci()
    
