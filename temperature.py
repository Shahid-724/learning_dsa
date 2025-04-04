# This code takes a string as input
# Prints the temperature in celcuis, fahrenheit and kelvin

# Taking input from the user
temp = input('Enter the temperature with unit: ')

# Declaring variables for different units of temperature
celsius = 0
fahrenheit = 0
kelvin = 0

# Converting the temperature 
if temp[-1].lower() == 'c':
    celsius = float(temp[:-1])
    fahrenheit = (9 * celsius / 5) + 32
    kelvin = celsius + 273

elif temp[-1].lower() == 'f':
    fahrenheit = float(temp[:-1])
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius + 273

else:
    kelvin = float(temp[:-1])
    celsius = kelvin - 273
    fahrenheit = (9 * celsius / 5) + 32

# Printing the output
print(f'{celsius:.2f}C')
print(f'{fahrenheit:.2f}F')
print(f'{kelvin:.2f}K')