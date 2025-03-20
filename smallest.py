# This code takes a list of integers as input
# Prints the smallest no from the list

# Taking input from the user
numbers = input('Enter space seperated no: ').split()

# Converting the list elements from strings to ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Printing the smallest number
print(min(numbers))