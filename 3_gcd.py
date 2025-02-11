# This code is used to find the gcd of two numbers
# Taking input from the user
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Declaring a variable to store the result
gcd = 1

# Calculating the gcd
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

# Printing the result
print(f'The gcd of {num1} and {num2} is {gcd}')