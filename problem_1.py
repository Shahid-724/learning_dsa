# This code takes four words as input 
# Prints the four words seperately

# Taking input from the user
words = input('Enter space seperated words: ').split()

# Declaring a variable for count
count = 1

# Printing the words
for i in words:
    print(f'word{count} = {i}')
    count += 1