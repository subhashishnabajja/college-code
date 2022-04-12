
memo = []
for i in range(20):
    memo.append(-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

for i in range(10):
    print(fib(i))