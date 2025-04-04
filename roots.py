# This code takes three integers as input
# Prints the roots of the quadratic equation

# Taking input from the user
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# Declaring variables for storing roots
root_1 = 0
root_2 = 0

# Calculating the determinant
det = b ** 2 - 4 * a * c

# Calculating the roots based on determinant
if det >= 0:
    root_1 = (-b + det ** 0.5) / (2 * a)
    root_2 = (-b - det ** 0.5) / (2 * a)

else:
    real = -b / (2 * a)
    imag = -det ** 0.5 / (2 * a)
    root_1 = complex(real, imag)
    root_2 = complex(real, -imag)

# Printing the output
print(f'{root_1:.2}')
print(f'{root_2:.2}')