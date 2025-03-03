# This code takes n lists as input
# Prints a list containing the max values from each list

# Taking input for n
n = int(input('Enter the no. of lists: '))

# Declaring a variable for max values
max_list = []

# Reading the lists and getting the max values
for i in range(n):
    numbers = input('> ').split()

    # Converting the list elements to ints
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    # Getting the max
    max_list.append(max(numbers))

# Printing the output
print(max_list)