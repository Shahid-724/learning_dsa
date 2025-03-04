# This code takes n lists as input
# Prints the lists without duplicates

# Taking input for n
n = int(input('How many lists: '))

# Declaring a list for output
result = []

# Reading the lists from the user
for i in range(n):
    numbers = input('> ').split()
    if len(numbers) == len(set(numbers)):
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        result.append(numbers)

# Printing the output
print(result)