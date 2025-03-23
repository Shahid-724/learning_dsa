# This code takes a string as input
# Prints a word using the next chars of this string

# Taking input from the user
word = input('Enter a string: ')

# Printing the output
for char in word: 
    print(chr(ord(char) + 1))