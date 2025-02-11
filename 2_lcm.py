# This code is used to find the lcm of two numbers
# Taking input from the user
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Declaring a variable to store lcm
lcm = max(num1, num2)
i = max(num1, num2)

# Calculating the lcm
while True:
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break
    i += 1

# Printing the result
print(f'The lcm of {num1} and {num2} is {lcm}')