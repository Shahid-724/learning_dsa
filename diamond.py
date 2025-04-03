# This code takes an integer as input
# Prints a diamond crystal

# Taking input from the user
n = int(input('Enter the size of the diamond: '))

# Printing the diamond
for i in range(2 * n):
    line = ''
    if i < n:
        line += ' ' * (n - i - 1) + '/' + ' ' * 2 * (i) + '\\'
    else:
        line += ' ' * (i - n) + '\\' + ' ' * 2 * (2 * n - i - 1) + '/'
    print(line)