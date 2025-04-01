# This code takes a string as input
# Prints the unicode value of the first uppercase char

# Taking input from the user
word = input('Enter a word: ')

# Printing the output
for char in word:
    if char.isupper():
        print(ord(char))
        break