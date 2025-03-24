# This code takes a string as input
# Prints the previous chars, ignores spaces

# Taking input from the user
word = input('Enter a string: ')

# Printing the previous chars
for char in word:
    if char == ' ':
        continue
    print(chr(ord(char) - 1))