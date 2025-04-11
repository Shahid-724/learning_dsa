# This code takes a string as input
# Prints the no. of uppercase and lowercase chars

# Defining the function
def count(word):

    # Declaring variable for counting upper and lower
    count_upper = 0
    count_lower = 0

    # Counting the chars
    for char in word:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1

    # Returning the counts
    return count_lower, count_upper

# Taking input from the user
user_word = input('Enter a word: ')

# Calling the function and storing the result
lower_count, upper_count = count(user_word)

# Printing the result
print(upper_count)
print(lower_count)