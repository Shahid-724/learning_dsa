# This code return the nth fibonacci term in the sequence
# Taking input from the user
n = int(input('Enter a number: '))

# Defining a function to return the nth fibo term recursively
def fibo_rec(num):
    if num <= 1:
        return num
    return fibo_rec(num - 1) + fibo_rec(num - 2)

# Calling the function and printing the output
print(fibo_rec(n))

# This is the non optimized version
