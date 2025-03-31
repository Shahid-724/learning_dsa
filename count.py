# This code takes two integers as input
# Prints the no. of chars with the given unicode

# Taking input from the user
word = input('Enter a string: ')
code = int(input('Enter the unicode: '))

# Declaring a variable for count
count = 0

# Counting the chars
for char in word: 
    if ord(char) == code:
        count += 1

# Printing the output
print(count)