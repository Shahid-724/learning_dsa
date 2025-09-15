# This code is used to calculate the power of a number using recursion
# Taking input from the user
num = int(input('Enter a number: '))
power = int(input('Enter the power: '))

# Defining an iterative function to calculate the power
def calc_power(num, power):
    result = 1
    for _ in range(power):
        result *= num
    return result

# Defining a recursive function to calculate the power
def cp_recur(num, power):
    if power == 0:
        return 1
    return num * cp_recur(num, power - 1)

# Calling the function and printing the output
print(calc_power(num, power))
print(cp_recur(num, power))