# This code takes two integers as input
# Prints the prime no. in that range

# Defining the function
def primes(num1, num2):

    # Declaring a variable for result
    result = ''

    # Checking for prime no
    for i in range(num1, num2 + 1):

        # Declaring a variable for counting the primes
        count = 0

        # Counting the factors
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                count += 1
                break

        # Adding the prime no to the string
        if not count:
            result += str(i) + ' '

    # Returning the result
    return result

# Taking input from the user
m = int(input('Enter the starting no: '))
n = int(input('Enter the ending no: '))

# Calling the function and storing the result
result = primes(m, n)

# Printing the result
print(result)