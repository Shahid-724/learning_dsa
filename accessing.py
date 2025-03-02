# This code takes n indices as input and has a list of lists
# Prints the elements at those indices

# Defining the lists
list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]

# Taking input for n
n = int(input('How many lists: '))

# Declaring a variable for storing the output
result = []

# Reading the input and getting the elements
for i in range(n):
    indices = input('> ').split()
    result.append(list_a[int(indices[0])][int(indices[1])])

# Printing the output
print(result)