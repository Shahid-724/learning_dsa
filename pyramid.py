# This code takes an integer as input
# Prints a horizontal pyramid

# Taking input from the user
n = int(input('Enter the size of the pyramid: '))

# Printing the pyramid
for i in range(2 * n):
    line = ''
    if i == 0 or i == 2 * n - 1:
        line += '|'
    elif i < n:
        line += '|' + ' ' * (i) + '\\'
    else:
        line += '|' + ' ' * (2 * n - i - 1) + '/'
    print(line)