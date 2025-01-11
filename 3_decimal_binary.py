# This code converts a decimal number to binary using recursion
# Taking input from the user
n = int(input('Enter a decimal number: '))

# Defining a recursive function to convert decimal to binary
def dec_bin(num):
    if not num:
        return ''
    return str(dec_bin(num // 2)) + str(num % 2)

# Calling the function and printing the output
print(dec_bin(n))