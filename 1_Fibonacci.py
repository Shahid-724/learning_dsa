# This code is used to get the nth fibonacci term using recursion and dp(memoization)

def fib(n, hashmap=dict()):
    if n in hashmap:
        return hashmap[n]
    if n <= 2:
        return 1
    hashmap[n] = fib(n - 1, hashmap) + fib(n - 2, hashmap)
    return hashmap[n]

n = int(input('Enter a number: '))
print(fib(n))