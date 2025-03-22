# This code takes a string as input
# Prints each char two times in the same line

# Taking input from the user
word = input('Enter a word: ')

# Printing the output
for char in word: 
    print(char * 2, end='')