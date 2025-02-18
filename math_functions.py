# Importing the math library
import math

# Declaring variables
pi = 3.1416
max = 180
angle = 0

# The logic to calculate cos and loop
while angle <= max:
    print(f'{str(angle).ljust(4)}  {math.cos(angle * pi / max):.4f}')
    angle += 10