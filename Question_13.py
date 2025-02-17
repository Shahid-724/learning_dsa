# Distance between two points
import math

# Taking input from the user
x1 = float(input('Enter the x-coordinate of the first point: '))
y1 = float(input('Enter the y-coordinate of the first point: '))
x2 = float(input('Enter the x-coordinate of the second point: '))
y2 = float(input('Enter the y-coordinate of the second point: '))

# Calculating the distance
dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'The distance between the two points is {dist:.3f}')