# This code takes a list of integers
# Prints the largest integers

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Converting the strings into ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Printing the largest number
print(max(numbers))