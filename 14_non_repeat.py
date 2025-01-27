# This code is used to find the non repeating elements in an array
# Taking an array as input from the user
nums = list(map(int, input('Enter space separated numbers: ').split()))

# Declaring a hashmap / dictionary to store the freqs of elements
freq_map = dict()

# Getting the elements and their counts into the hashmap
for i in nums:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1

# Printing the non - repeating elements
for i in nums:
    if freq_map[i] == 1:
        print(i, end=' ')