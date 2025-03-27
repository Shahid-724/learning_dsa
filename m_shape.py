# This code takes an integer as input
# Prints a m shape 

# Taking input from the user
n = int(input('Enter the size: '))

# Printing the m shape
for i in range(n):
    print('. ' * (n - i - 1) + '0 ' * (2 * i + 1) + '. ' * (2 * (n - i - 1)) + '0 ' * (2 * i + 1) + '. ' * (n - i - 1))