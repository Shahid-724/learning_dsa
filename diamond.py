# This code takes an integer as input
# Prints a hollow diamond using alphabets

# Taking input from the user
n = int(input('Enter the size of the diamond: '))

# Declaring a variable for alphabet
alphabet = 64

# Printing the diamond
for i in range(2 * n - 1):
    line = ''
    if i < n:
        alphabet += 1
        if i == 0:
            line += ' ' * (n - i - 1) + f'{chr(alphabet)} '
        else:
            line += ' ' * (n - i - 1) + f'{chr(alphabet)} ' + '  ' * (i - 1) + f'{chr(alphabet)}'
    else:
        alphabet -= 1
        if i == 2 * n - 2:
            line += ' ' * (i - n + 1) + f'{chr(alphabet)}'
        else:
            line += ' ' * (i - n + 1) + f'{chr(alphabet)} ' + '  ' * (2 * n - i - 3) + f'{chr(alphabet)}'
    print(line)
    