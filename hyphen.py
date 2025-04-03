# This code takes a string as input
# Prints the string with hyphens

# Taking input from the user
word = input('Enter a string: ')

# Printing the output
for i in range(len(word)):
    if i == len(word) - 1:
        print(word[i], end='')
    else:
        print(word[i] + '-', end='')