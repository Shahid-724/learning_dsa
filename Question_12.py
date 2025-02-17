# Arithmetic calculator
# Taking input from the user
number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))

# Printing the output in required format
print(f'x = {number_1}'.ljust(20) + f'y = {number_2}')
print(f'sum = {number_1 + number_2}'.ljust(20) + f'Difference = {number_1 - number_2}')
print(f'Product = {number_1 * number_2}'.ljust(20) + f'Division = {number_1 / number_2}')