# An integer is given as input
# Need to reverse the integer
# The integer should not be converted into a string

# Taking input from the user
num = int(input('Enter an integer: '))

# Declaring a variable for storing result
result = 0

# Checking for the negative sign
sign = 1
if num < 0:
    sign = -1
    num *= sign

# Looping through the num and adding it to result
while num:
    digit = num % 10
    result *= 10
    result += digit
    num //= 10

# Giving the result its sign
if sign == -1:
    result *= sign

# Printing the result
print(result)

# Code Works!