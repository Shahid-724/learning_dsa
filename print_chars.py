# This code takes two integers as input
# Prints the chars between those two values

# Taking input from the user
m = int(input('Enter the starting no: '))
n = int(input('Enter the ending no: '))

# Printing the chars
for i in range(m, n + 1):
    print(chr(i))