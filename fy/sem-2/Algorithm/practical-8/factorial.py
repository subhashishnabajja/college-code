def factorial(n):
    if n <= 1:
        return 1

    else:
        return n * factorial(n - 1)

print(factorial(5))


def factorialIter(n):
    fact = 1

    if n <= 1:
        return fact

    for i in range(1, n + 1):
        fact *= i


factorialIter(5)