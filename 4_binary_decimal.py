# This code converts a binary number to a decimal
# Taking input from the user
n = int(input('Enter a binary number: '))

# Declaring a variable for result, power
result = 0
power = 1

# Calculating the number
while n:
    result += (n % 10) * power
    power *= 2
    n //= 10

# Printing the result
print(f'The decimal number is {result}')