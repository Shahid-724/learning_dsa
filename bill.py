# This code takes an integer as input
# Prints the bill after discount

# Defining the function
def bill(amount):
    if amount < 500:
        return amount * 0.95
    elif 500 <= amount < 2500:
        return amount * 0.9
    else:
        return amount * 0.8
    
# Taking input from the user
total_amount = int(input('Enter your bill amount: '))

# Calling the function and storing the result
result = bill(total_amount)

# Printing the result
print(result)