# This code takes n lists as input
# Prints the max and min at index 0 and 1

# Taking input for n
n = int(input('How many lists: '))

# Declaring lists to store index 0 and index 1 elements
i0 = []
i1 = []

# Reading the lists
for i in range(n):
    numbers = input('> ').split()
    i0.append(int(numbers[0]))
    i1.append(int(numbers[1]))

# Getting the max and min values for each index
result_1 = max(i0), min(i0)
result_2 = max(i1), min(i1)

# Printing the output
print(result_1)
print(result_2)