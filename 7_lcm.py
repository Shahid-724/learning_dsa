# This code is used to find the lcm of two numbers using recursion
# Taking input from the user
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Defining an iterative function to find the lcm of two numbers
def lcm(n1, n2):
    i = max(n1, n2)
    while True:
        if i % n1 == 0 and i % n2 == 0:
            return i
        i += 1

# Defining a recursive function to find the hcf of two numbers
def lcm_rec(n1, n2):
    rem = n1 % n2
    if rem == 0:
        return n1
    return n1 * lcm_rec(n2, rem) // rem

# Calling the functions and printing the output
print(lcm(num1, num2))
print(lcm_rec(num1, num2))