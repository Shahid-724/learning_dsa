# This code takes 2 lists with people and their incomes
# Prints the name and id of the richest person

# Taking input from the user
n = int(input('Enter the no of test cases: '))

# Declaring lists for storing people's names and incomes
name_list = []
name_list1 = []
income_list = []

# Reading inputs and storing them in the lists
for i in range(n):
    cur_input = input('> ')
    cur_name = ''
    cur_income = ''
    names = cur_input.split()
    for i in names:
        name = ''
        if not i[0].isdigit():
            name += i
        name_list1.append(name)
    for i in cur_input:
        if i == ' ':
            continue
        if i.isdigit():
            cur_income += i
        else:
            cur_name += i.lower()
    if not cur_name in name_list:
        name_list.append(cur_name)
        income_list.append(int(cur_income))
    else:
        cur_index = name_list.index(cur_name)
        income_list[cur_index] += int(cur_income)

# Declaring a variable for result names
result_names = []

# Getting the result names
for i in range(len(income_list)):
    if income_list[i] == max(income_list):
        result_names.append(name_list[i])

# Sorting the result names list
result_names.sort()

# Getting the exact name and index
for i in name_list1:
    n = ''
    for j in i:
        if j == ' ':
            continue
        else:
            n += j
    if n == result_names[0]:
        print(i, name_list1.index(i))

# Printing the names and incomes
print(name_list)
print(name_list1)
print(income_list)
print(result_names[0])