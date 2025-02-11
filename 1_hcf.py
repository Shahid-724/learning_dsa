# This code is used to find the hcf of two numbers
# Taking input from the user
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Declaring a variable to store the hcf
hcf = 1

# Calculating the hcf
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

# Printing the result
print(f'The hcf of {num1} and {num2} is {hcf}')