# This code takes two integers as input
# Prints the sum of cubes in the range

# Defining the function
def cubes_sum(num1, num2):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i ** 3
    return sum

# Taking input from the user
m = int(input('Enter the starting no: '))
n = int(input('Enter the ending no: '))

# Calling the function and storing the result
result = cubes_sum(m, n)

# Printing the result
print(result)