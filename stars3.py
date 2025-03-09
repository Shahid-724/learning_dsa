# This code reads a word as input
# Prints the first and last letter 
# Prints stars for all the remaining letters 

# Taking input from the user
word = input('> ')

# Printing the output
print(word[0] + '*' * (len(word) - 2) + word[len(word) - 1])