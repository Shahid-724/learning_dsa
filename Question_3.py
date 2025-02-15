# Printing a multiplication table
# Taking input from the user
table = int(input('Enter the table that you want: '))

# The logic from printing the table 
for i in range(1, 11):
    print(f'{table} * {i} = {table * i}')