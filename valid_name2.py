# This code takes a string as input
# Checks whether it is a valid variable name

# Taking input from the user
word = input('Enter the name of your variable: ')

# Declaring a boolean to check 
is_valid = True

# Checking if it is valid
for char in word:
    if not char.isalnum() or word[0].isdigit():
        is_valid = False
    if char == '_':
        is_valid = True

# Printing the output
print(is_valid)