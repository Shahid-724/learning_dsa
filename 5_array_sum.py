# This code is used to find the sum of elements of an array
# Taking array as input
nums = list(map(int, input('Enter space separated numbers: ').split()))

# Declaring a variable to store the result
result = 0

# Iterating and getting the sum
for i in nums:
    result += i

# Printing the result
print(f'The sum of elements is {result}')