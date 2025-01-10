# This code is used to reverse a string recursively
# Taking input from the user for the string
s = input('Enter any string: ')

# Defining a function to reverse the string recursively
def reverse_string(string):
    # What is the base case
    # When an empty string is passed to the function, it returns an empty string
    if not string:
        return ''
    # What is the least amount of work that I can do in each iteration
    # The smallest unit of a string is a character
    # Changing the position of one character will be the least amount of work
    return reverse_string(string[1:]) + string[0]

# Calling the function and printing the result
print(reverse_string(s))