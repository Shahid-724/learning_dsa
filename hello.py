# Using the math module
import math

# Defining variables to be used
angle = 0
max = 180
pi = 3.1416

# The main logic to print cos values
while angle <= max: 
    print(f'{str(angle).ljust(4)} {math.cos(angle * pi / max):.4f}')
    angle += 10