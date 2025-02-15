# Printing the value of x for given a, b, c
# Taking input from the user
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

# Calculating and printing the output
print(f'The value of x is {a / (b - c):.2f}')

# If the value of b and c are equal, the program breaks and shows an error for division by zero