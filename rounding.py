# This code takes n floats as input
# Prints them rounded to two decimal places

# Taking input for n
n = int(input('How many numbers: '))

# Declaring a list for storing inputs
numbers = []

# Reading the no into the list
for i in range(n):
    numbers.append(float(input('> ')))

# Printing the output
for i in numbers:
    print(round(i, 2))