# This code is used to print the repeating elements from an array
# Taking input from the user for an array
nums = list(map(int, input('Enter space separated numbers: ').split()))

# Declaring a hashmap / dictionary to store the elements with freq
freq_map = dict()

# Getting the frequencies into the hashmap
for i in nums:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1

# Getting the repeating elements into another set
repeating_elements = set()
for i in nums:
    if freq_map[i] > 1 and i not in repeating_elements:
        repeating_elements.add(i)

# Printing the repeating elements
for i in repeating_elements:
    print(i, end=' ')