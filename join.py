# This code takes a string as input
# Prints the string joined by dots rather than spaces

# Taking input from the user
sentence = input('Enter a sentence: ')

# Splitting the sentence into words
words = sentence.split()

# Joining the sentence using .
result = '.'.join(words)

# Printing the result
print(result)