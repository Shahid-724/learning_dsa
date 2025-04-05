# This code takes a string as input
# Prints all chars that appear in dictionary order

# Taking input from the user
word = input('Enter a word: ')

# Declaring a variable for first char
first_char = word[0]
last_char = word[0]

# Checking for largest and smallest chars
for char in word:
    if char == ' ':
        continue
    if first_char > char:
        first_char = char
    if last_char < char:
        last_char = char
    
# Printing the output
print(first_char, last_char)