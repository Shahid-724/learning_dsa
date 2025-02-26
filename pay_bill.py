# Calculating the net salary of an employee
# Taking input from the user
basic_pay = float(input('Basic pay: '))
level = int(input('Job level: '))

# House rent allowance
hra = basic_pay / 4
gross_salary = 0
net_salary = 0

# Calculating gross salary
if level == 1:
    gross_salary = basic_pay + hra + 1500
elif level == 2:  
    gross_salary = basic_pay + hra + 950
elif level == 3: 
    gross_salary = basic_pay + hra + 600
else:
    gross_salary = basic_pay + hra + 250

# Calculating net salary
if gross_salary <= 2000:
    net_salary = gross_salary
elif 2001 <= gross_salary <= 4000:
    net_salary = gross_salary * 97 / 100
elif 4001 <= gross_salary <= 5000:
    net_salary = gross_salary * 95 / 100
else:
    net_salary = gross_salary * 92 / 100

print(f'Your salary is {net_salary}')
