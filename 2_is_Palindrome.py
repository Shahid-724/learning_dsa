# This code checks whether a string is a palindrome or not recursively
# Taking input from the user for the string
s = input('Enter a string: ')

# Defining a recursive function to check if a string is palindrome
def is_palindrome(string):
    # What is the base case
    # The first base case
    if len(string) <= 1:
        return True
    # The second base case:
    if string[0] != string[-1]:
        return False
    
    # What is the smallest amount of work that can be done 
    return is_palindrome(string[1:-1])

# Calling the function and printing the output
print(is_palindrome(s))