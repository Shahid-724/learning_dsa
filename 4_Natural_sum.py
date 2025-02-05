# This code is used to print the sum of first n natural nums

def nat_sum(n):
    result = n * (n + 1) // 2
    for i in range(1, n + 1):
        print(i, end=' ')
        if i != n:
            print('+', end=' ')
    print('=', result)

n = int(input('Enter a number: '))
nat_sum(n)