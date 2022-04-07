def fibonacci(n, t1, t2):
    if n <= 1:
        return
    
    else:
        print(t1)
        fibonacci( n - 1, t2, t1 + t2)


fibonacci(20, 0, 1)


def fibonacciIter(n):
    t1 = 0
    t2 = 1
    fib = 0
    print(t1, "\n", t2)
    for i in range(n):
        fib = t1 + t2
        t1 = t2
        t2 = fib
        print(fib)
fibonacciIter(20)