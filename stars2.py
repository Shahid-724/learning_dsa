# This code reads a word as input
# Prints stars on either side of the word
# The no. of stars is equal to the length of the word

# Taking input from the user
word = input('> ')

# Printing the output
print('*' * len(word) + ' ' + word + ' ' + '*' * len(word))