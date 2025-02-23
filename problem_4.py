# This code takes a string as input
# Prints the no. of vowels and consonants

# Taking input from the user
word = input('Enter a word: ')

# Declaring variables for vowel and consonant count
vowels = 0
consonants = 0

# Declaring a list for vowels
vowel_list = ['a', 'e', 'i', 'o', 'u']

# Counting the vowels and consonants
for char in word: 
    if char.lower() in vowel_list:
        vowels += 1
    else:
        consonants += 1

# Printing the output
print(f'Number of vowels = {vowels}')
print(f'Number of consonants = {consonants}')