# This code takes two integers as input
# Prints 32 power n where n is the diff between the two ints

# Taking input from the user
numbers = input('Enter the magnitudes: ').split()

# Calculating the power
power = abs(int(numbers[0]) - int(numbers[1]))

# Calculating and printing the output
print(32 ** power)