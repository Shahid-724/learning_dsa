# Converting Fahrenheit to Celcius 
# Declaring variables
fahrenheit = 0
max = 250

print('Fahrenheit'.ljust(12) + 'Celcius')

# The logic for conversion and printing
while fahrenheit <= max:
    celcius = (fahrenheit - 32) * 5 / 9
    print(f'{str(fahrenheit)}'.ljust(12) + f'{celcius:.2f}')
    fahrenheit += 25
