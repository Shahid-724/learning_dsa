# This code takes a string as input
# Changes the first letter every word

# Taking input from the user
sentence = input('Enter a string: ')

# Splitting the sentences into words
words = sentence.split()

# Changing the first letter of every word and printing
for word in words:
    new_word = chr(ord(word[0]) + 1) + word[1:]
    print(new_word, end=' ')