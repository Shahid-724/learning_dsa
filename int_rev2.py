# An integer is given as input
# Need to reverse the integer
# by converting it into a string

# Taking input from the user
num = int(input('Enter a number: '))

# Declaring a variable to store the result
reverse = ''

# Checking for the sign
sign = 1
if num < 0:
    sign = -1
    num *= sign

# Converting the input number into an string
num = str(num)

# Looping through the string
for i in num:
    reverse = i + reverse

# Converting the reversed string to integer
reverse = int(reverse)

# Giving the reversed number it's sign
reverse *= sign

# Printing the output
print(reverse)

# Code Works!