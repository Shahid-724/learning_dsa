# This code takes an integer as input
# Prints the no. of cars required for n people
import math

# Defining the function
def cars(people):
    return math.ceil(people / 5)

# Taking input from the user
n = int(input('Enter the no. of people: '))

# Calling the function and storing the result
result = cars(n)

# Printing the result
print(result)