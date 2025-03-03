# This code has a list of tuples and takes an integer as input
# Prints the index of that numbers

# Defining the list of tuples
num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]

# Taking input from the user
n = int(input('Enter a number: '))

# Declaring a variable to store the result
result = ''

# Getting the indices to the result
for i in range(len(num_list)):
    if n in num_list[i]:
        result += str(i) + ' ' + str(num_list[i].index(n))

# Printing the output
print(result)