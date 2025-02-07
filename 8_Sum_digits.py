# This code is used to get the sum of digits of a number using recursion

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

n = int(input('Enter a number: '))
print(sum_digits(n))