# This code is used to find the sum of first n natural numbers
# Taking input from the user
n = int(input('Enter a number: '))

# Defining a recursive function to get the sum of first n natural numbers
def natural_num_sum(num):
    if not num:
        return 0
    return num + natural_num_sum(num - 1)

# Calling the function and printing the output
print(natural_num_sum(n))