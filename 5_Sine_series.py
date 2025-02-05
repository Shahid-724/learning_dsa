# This code is used to find the sum of sine series

import math

def sine(x, n):
    series_sum = 0
    pi = 22 / 7
    y = x * (pi / 180)
    for i in range(n):
        sign = (-1) ** i
        series_sum += (y ** (2 * i + 1)) / math.factorial(2 * i + 1) * sign
    return round(series_sum, 2)

x = int(input('Enter the angle: '))
n = int(input('Enter the no. of terms: '))
print(sine(x, n))