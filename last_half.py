# This code takes a list of integers 
# Prints the last half of the list

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Converting the list of string into ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Printing the last half of the list
print(numbers[(-len(numbers) + 1) // 2:])