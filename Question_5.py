# Temperature conversion
# Taking input from the user
temp = float(input('Enter the temperature: '))
convert = input('Press...\nF for Fahrenheit...\nC for Celcuis...\n')

# The logic for converting temperature and printing
if convert.lower() == 'f':
    print(f'The temperature in Fahrenheit is {(9 * temp / 5) + 32}')
else: 
    print(f'The temperature in Celcius is {(temp - 32) * 5 / 9}')
