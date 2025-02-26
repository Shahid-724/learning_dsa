# Reading multiple inputs from the user and calculating average and range
# Taking input from the user
n = int(input('How many inputs? '))

# Declaring variables for use
data_list = []
sum = 0

# Loop to take multiple into an array
for i in range(0, n):
    data_item = float(input('> '))
    data_list.append(data_item)
    sum += data_item

# The calculation and printing of data
print(f'Total values: {n}')
print(f'Highest value: {max(data_list)}')
print(f'Lowest value: {min(data_list)}')
print(f'Range: {max(data_list) - min(data_list):.2f}')
print(f'Average: {sum / n}')