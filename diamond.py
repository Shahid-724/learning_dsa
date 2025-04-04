# This code takes an integer as input
# Prints a hollow diamond using continuous alphabets

# Taking input from the user
n = int(input('Enter the size of the diamond: '))

# Declaring a variable for alphabets
alphabet = 65

# Printing the diamond
for i in range(2 * n - 1):
    line = ''
    if i == 0 or i == 2 * n - 2:
        line += ' ' * (n - 1) + 'A'
    elif i < n:
        line += ' ' * (n - i - 1)
        for j in range(2):
            alphabet += 1
            line += f'{chr(alphabet)}' + ' ' * (2 * i - 1)
    else:
        line += ' ' * (i - n + 1)
        alphabet -= 3
        for j in range(2):
            line += f'{chr(alphabet)} ' + '  ' * (2 * n - i - 3)
            alphabet += 1
        alphabet -= 1
    print(line)