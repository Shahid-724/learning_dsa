# Interest calculation from year 1

# Taking input from the user
principal = float(input('Enter the principal: '))
int_rate = float(input('Enter the rate of interest: '))
time_period = float(input('Enter the time period: '))

# Declaring variables for use in the program
year = 0
value = 0

# The main logic to calculate and print the interest
while year < time_period: 
    value = principal * (1 + int_rate / 100)
    year += 1
    principal = value
    print(f'{str(year).ljust(4)} {principal:.2f}')