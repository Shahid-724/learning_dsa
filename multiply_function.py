# Defining the function
def multiply(num1, num2):
    return num1 * num2

# Taking user input
number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))

# Calling the function and printing the output
product = multiply(number_1, number_2)
print(f'The product is {product}')