# This code takes a string as input
# Prints the words in reverse order

# Taking input from the user
sentence = input('Enter a sentence: ')

# Splitting the sentence
words = sentence.split()

# Reversing the words
words = words[::-1]

# Joining the words
words = ' '.join(words)

# Printing the output
print(words)