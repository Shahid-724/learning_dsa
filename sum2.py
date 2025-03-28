# This code takes two integers as input
# Prints the sum of series upto n powers 
# Rounds the sum to 4 decimal places

# Taking input from the user
x = float(input('Enter a number: '))
n = int(input('Enter the no. of terms: '))

# Declaring a variable for sum
sum = 0

# Calculating the sum
for i in range(n):
    sum += x ** (i + 1)

# Printing the sum
print(round(sum, 4))