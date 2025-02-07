# This code is used to find the lcm of two nums using recursion

def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)

def lcm(a, b):
    return a * b // hcf(a, b)

a = int(input('Enter first num: '))
b = int(input('Enter second num: '))
print(lcm(a, b))