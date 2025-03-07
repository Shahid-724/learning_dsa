# This code takes a list and n queries as input
# Prints the no of elements that are greater than q

# Taking input for n and q
n, q = input('Enter height and queries: ').split()

# Reading the numbers
numbers = input('Enter space seperated numbers: ').split()

# Converting the list elements to ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Declaring a variable for result
result = ''

# Reading the queries and adding it to the result
for i in range(int(q)):
    query = int(input('> '))
    temp = []
    for j in range(len(numbers)):
        if numbers[j] > query:
            temp.append(numbers[j])
    result += str(len(temp)) + '\n'

# Printing the output
print(result)