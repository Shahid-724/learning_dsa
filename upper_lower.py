# This code takes a string as input
# Prints the uppercase and lowercase chars on a seperate line

# Defining the function
def upper_lower(word):

    # Declaring variable for storing char
    upper = ''
    lower = ''

    # Adding chars to the variables
    for char in word:
        if char.isupper():
            upper += char
        else:
            lower += char

    # Returning the variables
    return upper, lower

# Taking input from the user
user_word = input('Enter a word: ')

# Calling the function and storing the result
upper_case, lower_case = upper_lower(user_word)

# Printing the output
print(upper_case)
print(lower_case)