# To calculate the salary of a salesman
# Defining variables
base_salary = 1500
bonus_per_computer = 200
commission = 0.02

# Taking input from the user
computers_sold = int(input('Enter the no. of computers sold: '))
computer_price = float(input('Enter the price of each computer: '))

# The calculations
bonus = computers_sold * bonus_per_computer
commission = computers_sold * commission * computer_price
gross_salary = base_salary + bonus + commission

# Printing the output
print('Bonus'.ljust(15) + ' = ' + f'{bonus:.2f}')
print('Commission'.ljust(15) + ' = ' + f'{commission:.2f}')
print('Gross Salary'.ljust(15) + ' = ' + f'{gross_salary:.2f}')