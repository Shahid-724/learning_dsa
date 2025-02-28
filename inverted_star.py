# This code is used to print an inverted right triangle pattern

def inv_pattern(n):
    for i in range(n):
        print(' ' * i + '*' * (n - i))

n = int(input('Enter a number: '))
print(inv_pattern(n))