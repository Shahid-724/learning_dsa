# This code takes a string as input
# Prints the frequency of each char in alphabetical order

# Taking input from the user
word = input('Enter a word: ').lower()

# Converting the word to a set to remove duplicates
chars = sorted(list(set(word)))

# Counting and printing the frequency
for i in chars:
    if i == ' ':
        continue
    print(f'{i}: {word.count(i)}')