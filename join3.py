# This code takes a string as input
# Prints the third letter of every word seperated by comma

# Taking input from the user
sentence = input('Enter a sentence: ')

# Splitting the sentence into words
words = sentence.split()

# Declaring a variable for storing result
result = []

# Looping through the words list
for word in words:
    result += word[2]

# Joining the chars from the result
result = ','.join(result)

# Printing the result
print(result)