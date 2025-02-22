# To find the roots of a quadratic equation
import math

# Taking input from the user for a, b and c
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))

# Empty variables for roots
root_1 = 0
root_2 = 0

# Calculating the determinant to know the nature and type of roots
det = b ** 2 - 4 * a * c

# Calculating the roots
if det > 0:
    root_1 = (-b + math.sqrt(det)) / (2 * a)
    root_2 = (-b - math.sqrt(det)) / (2 * a)
elif det == 0:
    root_1 = root_2 = -b / (2 * a)
else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-det) / (2 * a)
    root_1 = complex(real, imaginary)
    root_2 = complex(real, -imaginary)

# Printing the roots
print(f'The roots of the given quadratic equation are {root_1:.2} and {root_2:.2}')
