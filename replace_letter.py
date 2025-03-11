# This code takes three inputs
# A word, an index and a char
# Replaces the char at index with the new char

# Taking input from the user
word = input('Enter the word: ')
index = int(input('Enter the index: '))
char = input('Enter the character: ')

# Printing the output
print(word[:index] + char + word[index + 1:])