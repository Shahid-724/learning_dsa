# This code takes two integers as input
# Checks whether the addition generates a carry

# Doing this with numbers as strings is easy
# So I am going to take the input in the form of string

# Taking input from the user
num1, num2 = input('Enter space seperated numbers: ').split()

# Declaring a variable for checking carry
carry = False

# Checking for carry
for i in range(min(len(num1), len(num2))):
    if int(num1[len(num1) - i - 1]) + int(num2[len(num2) - i - 1]) > 9:
        carry = True
        break

# Printing the result
if carry:
    print('Hard')
else:
    print('Easy')