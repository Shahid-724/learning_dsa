# This code takes n lists as input
# Creates a nested lists containing n lists

# Taking input for the no. of lists
n = int(input('How many lists: '))

# Declaring a list variable for storing lists
nested_lists = []

# Reading the lists and storing them
for i in range(n):
    numbers = input('> ').split()

    # Converting the list elements to ints
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    nested_lists.append(numbers)

# Printing the output
print(nested_lists)