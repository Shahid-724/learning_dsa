# This code takes a string as input
# Prints whether it is valid or not using a function

# Defining function
def atm_pin_validation(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return 'Valid PIN code'
    else:
        return 'Invalid PIN code'
    
# Taking input from the user
atm_pin = input('Enter your atm pin: ')

# Calling the function and storing the result
result = atm_pin_validation(atm_pin)

# Printing the result
print(result)