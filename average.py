# This code takes two integers as input
# Prints the sum and average for all no in that range

# Taking input from the user
m = int(input('Enter the starting no: '))
n = int(input('Enter the ending no: '))

# Declaring a variable for sum
sum = 0

# Calculating the sum
for i in range(m, n + 1):
    sum += i

# Printing the output
print(sum)
print(sum / (n - m + 1))