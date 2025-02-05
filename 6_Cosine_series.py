# This code is used to find the cosine series sum for a given angle and no. of terms

import math

def cosine_sum(x, n):
    series_sum = 1
    sign = -1
    pi = 22 / 7
    y = x * (pi / 180)
    for i in range(2, n, 2):
        series_sum += sign * (y ** i) / math.factorial(i)
        sign = -sign
    return round(series_sum, 2)

x = int(input('Enter the value of x: '))
n = int(input('Enter the value of n: '))
print(cosine_sum(x, n))