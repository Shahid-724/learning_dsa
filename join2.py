# This code takes a string as input
# Prints the string with seperator comma instead of space

# Taking input from the user
sentence = input('Enter space seperated numbers: ')

# Seperating the numbers
numbers = sentence.split()

# Joining the numbers with comma
result = ','.join(numbers)

# Printing the result
print(result)