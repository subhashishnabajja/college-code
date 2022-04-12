import time
import numpy as np
import sys
from matplotlib import pyplot


def fibonacci(n, t1, t2):
    if n <= 1:
        return
    
    else:
        print(t1)
        fibonacci( n - 1, t2, t1 + t2)


fibonacci(6, 0, 1)


def fibonacciIter(n):
    t1 = 0
    t2 = 1
    fib = 0
    print(t1)
    print(t2)
    for i in range(n - 2):
        fib = t1 + t2
        t1 = t2
        t2 = fib
        print(fib)
fibonacciIter(5)



nums = []
times = []

for num in range(100):
    start_time = time.perf_counter()
    fibonacciIter(num)
    elapsed_time = time.perf_counter() - start_time
    nums.append(num)
    times.append(elapsed_time)

  

pyplot.xlabel("Number")
pyplot.ylabel("Time (in seconds)")
pyplot.title('Fibonacci Iterative')
pyplot.plot(nums, times)

pyplot.show()   