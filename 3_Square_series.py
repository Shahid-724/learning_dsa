# This code is used to compute the sum of square series

def square_series(x, n):
    result = 1
    for i in range(2, n + 1):
        result += x ** i / i
    return round(result, 2)

x = int(input('Enter value of x: '))
n = int(input('Enter value of n: '))
print(square_series(x, n))