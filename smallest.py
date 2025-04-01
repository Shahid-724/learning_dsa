# This code takes a string as input
# Prints the char with smallest unicode value

# Taking input from the user
word = input('Enter a word: ')

# Declaring a variable for smallest char
smallest = 122

# Checking for the smallest value
for char in word:
    if smallest > ord(char):
        smallest = ord(char)

# Printing the output
print(chr(smallest))