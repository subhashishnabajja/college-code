memo = [ -1 for _ in range(20)]


def factorial(n):
    if n <= 1:
        return 1
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = n * factorial(n - 1)
    return memo[n]

print(factorial(5))
