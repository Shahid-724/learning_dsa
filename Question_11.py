# Area of the triangle using semi-perimeter
import math

# Taking input from the user
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

# Calculating the semi-perimeter and area
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f'The area is {area} sq units')