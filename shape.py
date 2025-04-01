# This code takes an integer as input
# Prints a shape using $s

# Taking input from the user
n = int(input('Enter the size of the shape: '))

# Printing the shape
for i in range(n):
    print(' ' * (n - i - 1) + '$' * n)