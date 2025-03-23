# This code takes a string as input
# Prints the first and last words in the dictionary order

# Taking input from the user
sentence = input('Enter a sentence: ')

# Splitting the sentence into words
words = sentence.split()
print(words)

# Declaring variables for first and last words
first_word = words[0]
last_word = words[0]

# Checking for the first and last words
for word in words:
    if first_word.lower() > word.lower():
        first_word = word
        print(word)
        print(first_word)
    if last_word.lower() < word.lower():
        last_word = word

# Printing the output
print(first_word, last_word)