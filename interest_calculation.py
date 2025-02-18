# Defining variables
year = 0
value = 0

# Taking user input for principal, interest rate and period
principal = int(input('Enter the principal: '))
int_rate = float(input('Enter the Rate of Interest: '))
period = int(input('Enter the period: '))

# Logic for compound interest calculation
while year <= period:
    print(f'{str(year).ljust(4)}    {principal:.2f}')
    value = principal * (1 + int_rate / 100)
    principal = value
    year += 1