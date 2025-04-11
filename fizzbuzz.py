# This code takes an integer as input
# Prints fizzbuzz or the number

# Defining the function
def fizzbuzz(n):
    result = ''
    if n % 3 == 0:
        result += 'Fizz'
    if n % 5 == 0:
        result += 'Buzz'

    if result == '':
        result = n

    return result

# Taking input from the user
number = int(input('Enter a number: '))

# Calling the function and storing the result
result = fizzbuzz(number)

# Printing the result
print(result)