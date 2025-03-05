# This code takes a list of integers 
# Prints their product

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Declaring a variable for product
prod = 1

# Calculating the product 
for i in numbers:
    prod *= int(i)

# Printing the product
print(prod)