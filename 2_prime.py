# This code checks whether a number is prime or not recursively
# Taking input from the user
n = int(input('Enter a number: '))

# Defining an iterative function to check for prime
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Defining a recursive function to check for prime
def is_prime_rec(num, div=2):
    if div == int(num ** 0.5) + 1:
        return True
    if num % div == 0:
        return False
    return is_prime_rec(num, div + 1)

# Calling the function and printing the output
print(is_prime(n))
print(is_prime_rec(n))