# This code takes n lists as input
# Prints a list of tuples as output

# Taking input from the user
n = int(input('How many lists: '))

# Declaring a list to store tuples
tuple_list = []

# Reading the lists and converting to tuples
for i in range(n):
    numbers = input('> ').split()

    # Converting the list elements to ints
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    # Converting list to tuple and appending
    tuple_list.append(tuple(numbers))

# Printing the output
print(tuple_list)