# This code takes an integer as input
# Prints a hollow m shape with alphabets

# Taking input from the user
n = int(input('Enter the size: '))

# Declaring a variable for alphabet
alphabet = 64

# Printing the m shape
for i in range(n):
    alphabet += 1
    if i == 0:
        print(' ' * (n - i - 1) + f'{chr(alphabet)} ' + '  ' * (n - i - 1) + f'{chr(alphabet)}')
    else:
        print(' ' * (n - i - 1) + f'{chr(alphabet)} ' + '  ' * (i - 1) + f'{chr(alphabet)} ' + '  ' * (n - i - 1) + f'{chr(alphabet)} ' + '  ' * (i - 1) + f'{chr(alphabet)}')