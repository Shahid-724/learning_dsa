# This code takes a string as input
# Prints the next char of every char 
# Space char does not change

# Taking input from the user
word = input('Enter a string: ')

# Changing the chars
for char in word: 
    if char == ' ':
        print(' ', end='')
    else:
        print(chr(ord(char) + 1), end='')