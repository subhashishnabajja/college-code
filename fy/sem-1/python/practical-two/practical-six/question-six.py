def fibonnaci(num):
    i = 0
    t1 = 0
    t2 = 1
    t3 = 0

    fib = []

    
    while i <= num:
        fib.append(t1)
        t3 = t2 + t1
        t1 = t2
        t2 = t3
        i += 1

    print(*fib)



fibonnaci(50)
