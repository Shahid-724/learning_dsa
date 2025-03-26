# This code takes an integer as input
# Prints a hollow diamond

# Taking input from the user
n = int(input('Enter the size of the diamond: '))

# Printing the diamond
for i in range(2 * n):
    if i < n:
        print('* ' * (n - i) + '  ' * 2 * i + '* ' * (n - i))
    else:
        print('* ' * (i - n + 1) + '  ' * 2 * (2 * n - i - 1) + '* ' * (i - n + 1))