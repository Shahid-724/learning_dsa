# This code is used to find the hcf of two numbers

def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)

a = int(input('Enter first num: '))
b = int(input('Enter second num: '))
print(hcf(a, b))