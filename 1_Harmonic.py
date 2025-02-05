# This code is used to calculate the sum of first n terms of a harmonic progression

def harmonic(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / i
    return round(result, 2)

n = int(input('Enter a number: '))
print(harmonic(n))