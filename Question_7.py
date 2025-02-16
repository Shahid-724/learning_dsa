# Function for sum and difference
# Taking input from the user
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

# Defining a function for addition
def add(num1=0, num2=0):
    return num1 + num2

# Defining a function for subtraction
def sub(num1=0, num2=0):
    return num1 - num2

# Calling the functions and storing the outputs
sum = add(number_1, number_2)
difference = sub(number_1, number_2)

# Displaying the output in required format
print(f'{number_1} + {number_2} = {sum}')
print(f'{number_1} - {number_2} = {difference}')