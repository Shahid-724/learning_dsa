# This code takes a string as input
# Prints the time in hours

# Taking input from the user
time = input('Enter the time: ')

# Calculating the result
if time[-1].lower() == 's':
    print(f'{round(float(time[:-1]) / 3600, 2)}H')
else:
    print(f'{round(float(time[:-1]) / 60, 2)}H')