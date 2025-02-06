# This code is used to find the factorial of a num using recursion

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

n = int(input('Enter a number: '))
print(fact(n))