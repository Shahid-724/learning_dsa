# The coordinates of diameter touching two ends of a circle are given, find the area of the circle
import math

# Taking input from the user
x1 = float(input('Enter the x-coordinate of the first point: '))
y1 = float(input('Enter the y-coordinate of the second point: '))
x2 = float(input('Enter the x-coordinate of the first point: '))
y2 = float(input('Enter the y-coordinate of the second point: '))

# Calculating the radius
radius = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) / 2

# Calculating the area and printing the output
area = math.pi * radius * radius
print(f'The area of the circle of radius {radius:.2f} is {area:.2f}')