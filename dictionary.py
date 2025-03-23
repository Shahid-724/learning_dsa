# This code takes a string as input
# Prints the word that comes first in dictionary order

# Taking input from the user
sentence = input('Enter a string: ')

# Splitting the sentence into words
words = sentence.split()

# Declaring a variable to hold the first word
first_word = words[0]

# Checking the list for the first word
for word in words:
    if first_word.lower() > word.lower():
        first_word = word

# Printing the output
print(first_word)