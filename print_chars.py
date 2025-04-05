# This code takes three inputs
# A string and two integers
# Prints all the chars between those two unicode values from the string

# Taking input from the user
word = input('Enter a string: ')
m = int(input('Enter the starting no: '))
n = int(input('Enter the ending no: '))

# Checking for the chars and printing
for char in word:
    if m <= ord(char) <= n:
        print(char, end=' ')