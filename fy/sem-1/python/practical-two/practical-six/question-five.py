def factorial(num):
    i = 1
    result = i

    while i <= num:
        result *= i
        i+=1
    return result


fact = int(input("Enter a number: "))

print(factorial(fact))
