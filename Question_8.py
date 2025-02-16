# Adding border lines to the address
# Taking input from the user
name = input('Enter your name: ')
door_no = input('Enter your door no.: ')
street = input('Enter your street: ')
city = input('Enter your city: ')
pin_code = input('Enter your pincode: ')

# Defining variables for borders
top_and_bottom = '-'.ljust(25, '-')

# Printing the output
print(top_and_bottom)
print(f'| {name}'.ljust(25) + '|')
print(f'| {door_no}, {street}'.ljust(25) + '|')
print(f'| {city}, {pin_code}'.ljust(25) + '|')
print(top_and_bottom)