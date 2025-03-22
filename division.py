# This code takes n inputs 
# Prints their quotient when divided by 17

# Taking input from the user
n = int(input('How many inputs: '))

# Declaring a list to store inputs
numbers = []

# Reading inputs from the user
for i in range(n):
    numbers.append(int(input('> ')))

# Printing the output
for i in numbers:
    print(i // 17)