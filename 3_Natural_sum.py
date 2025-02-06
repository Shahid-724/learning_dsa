# This code is used to find the sum of first n natural no

def nat_sum(n):
    if n == 0:
        return 0
    return n + nat_sum(n - 1)

n = int(input('Enter a number: '))
print(nat_sum(n))