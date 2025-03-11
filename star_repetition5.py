# This code takes two words as input
# Prints the second word in stars and then remaining part of the first word

# Taking input from the user
word1 = input('> ')
word2 = input('> ')

# Printing the output
print('*' * len(word2) + word1[len(word2):])