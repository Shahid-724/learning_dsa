# Calculating the radius from a point on a circle with center on the origin
import math

# Taking input from the user 
x = float(input('Enter the x-coordinate of the point: '))
y = float(input('Enter the y-coordinate of the point: '))

# Calculating the radius
radius = math.sqrt(abs(x ** 2 - y ** 2))

# Calculating the area of the circle 
area = math.pi * radius * radius
print(f'The area of the circle is {area:.2f}')