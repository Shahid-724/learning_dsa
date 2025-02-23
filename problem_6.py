# This code takes a string as input
# Prints a pattern using the string

# Taking input from the user
word = input('Enter a word: ')

# Printing the pattern
for i in range(2 * len(word) - 1):
    if i <= len(word):
        print(word[:i + 1])
    else:
        print(word[:len(word) - i - 1])