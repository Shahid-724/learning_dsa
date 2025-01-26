# This code is used to find the frequency of each element in an array
# Taking input for an array from the user
nums = list(map(int, input('Enter space separated numbers: ').split()))

# Declaring a hashmap / dictionary to store the frequency of each element
freq_map = dict()

# Getting the frequency of each element
for i in nums:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1

# Printing the hashmap to show the frequencies
print(freq_map)