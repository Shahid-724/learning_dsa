# This code takes an integer as input
# Prints a diamond using 0s and dots

# Taking input from the user
n = int(input('Enter the size of the diamond: '))

# Printing the diamond
for i in range(2 * n - 1):
    line = ''
    if i < n:
        line += '. ' * (n - i - 1) + '0 ' * (2 * i + 1) + '. ' * (n - i - 1)
    else:
        line += '. ' * (i - n + 1) + '0 ' * (2 * (2 * n - i - 1) - 1) + '. ' * (i - n + 1)
    print(line)