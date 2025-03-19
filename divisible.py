# This code takes a list of integers as input
# Prints a list of no divisible by 3

# Taking input from the user
numbers = input('Enter space seperated numbers: ').split()

# Declaring a list for no divisible by 3
divisible = []

# Getting the elements into the list
for i in numbers:
    if int(i) % 3 == 0:
        divisible.append(int(i))

# Printing the list
print(divisible)