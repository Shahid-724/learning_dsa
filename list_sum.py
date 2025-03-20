# This code takes a list of numbers as input
# Prints the sum of elements of the list

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Declaring a variable for storing sum
sum = 0

# Calculating the sum
for i in numbers:
    sum += int(i)

# Printing the sum 
print(sum)