# This code has a list of tuples and takes an integer as input
# Prints the list of tuples after removing n

# Defining the list of tuples
num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]

# Taking input from the user
n = int(input('Which element do you want to remove: '))

# Removing the element from all tuples
for i in range(len(num_list)):
    if n in num_list[i]:
        current_list = list(num_list[i])
        current_list.remove(n)
        num_list[i] = tuple(current_list)

# Printing the output
print(num_list)