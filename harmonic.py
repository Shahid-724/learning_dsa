# This code takes an integer as input
# Prints the sum of n terms of the harmonic series

# Taking input from the user
n = int(input('Enter the no. of terms: '))

# Declaring a variable for storing sum
sum = 0

# Calculating the sum
for i in range(n):
    sum += 1 / (i + 1)

# Printing the sum
print(round(sum, 2))