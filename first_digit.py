# This code takes a string as input
# Prints the unicode value of the first digit

# Taking input from the user
word = input('Enter a word: ')

# Checking for the first digit in the input
for char in word:
    if char.isdigit():
        print(ord(char))
        break