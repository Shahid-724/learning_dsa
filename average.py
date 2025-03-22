# This code takes n integers as input
# Prints their cumulative average

# Taking input for n
n = int(input('How many numbers: '))

# Declaring a list for storing no
numbers = []

# Reading the input from user
for i in range(n):
    numbers.append(int(input('> ')))

# Declaring a variable for sum
sum = 0

# Calculating and printing the average
for i in range(len(numbers)):
    sum += numbers[i]
    print(round(sum / (i + 1), 2))