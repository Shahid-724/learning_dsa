# This code is used to compute the fibonacci term recursively but it is also optimized
# Taking input from the user for n
n = int(input('Enter a number: '))

# Creating a hashmap to store the temporary values
fibo_hash = {1: 1, 0: 1}

# Defining a recursive and optimized function for fibonacci
def fibo(num):
    if num in fibo_hash:
        return fibo_hash[num]
    result = fibo(num - 1) + fibo(num - 2)
    fibo_hash[num] = result
    return result

# Calling the function and printing the result
print(fibo(n))