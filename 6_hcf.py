# This code is used to find the hcf of two numbers using recursion
# Taking input from the user
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Defining an iterative function to get hcf
def hcf(n1, n2):
    result = 1
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            result = i
    return result

# Defining a recursive function to get hcf
def hcf_rec(n1, n2):
    n1, n2 = max(n1, n2), min(n1, n2)
    if n1 % n2 == 0:
        return n2
    return hcf_rec(n2, n1 % n2)

# Calling the functions and printing the output
print(hcf(num1, num2))
print(hcf(num1, num2))