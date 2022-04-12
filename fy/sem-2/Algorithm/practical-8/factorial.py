import time
import numpy as np
import sys
from matplotlib import pyplot




def factorial(n):
    if n <= 1:
        return 1

    else:
        return n * factorial(n - 1)




def factorialIter(n):
    fact = 1

    if n <= 1:
        return fact

    for i in range(1, n + 1):
        fact *= i


nums = []
times = []

for num in range(100):
    start_time = time.perf_counter()
    factorialIter(num)
    elapsed_time = time.perf_counter() - start_time
    nums.append(num)
    times.append(elapsed_time)

  

pyplot.xlabel("Number")
pyplot.ylabel("Time (in seconds)")
pyplot.title('Factorial Iterative')
pyplot.plot(nums, times)

pyplot.show()   
