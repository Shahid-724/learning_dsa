# Interest calculation similar to the one in chapter 1
# Taking input from the user
principal = float(input('Enter the principal: '))
int_rate = float(input('Enter the rate of interest: '))
time_period = float(input('Enter the time period: '))

# Declaring variables for use in the logic
year = 0
value = 0

# The main logic for calculating interest and printing
while year <= time_period:
    print(f'{str(year).ljust(4)} {principal:.2f}')
    value = principal * (1 + int_rate / 100)
    principal = value
    year += 1