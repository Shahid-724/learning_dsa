# This code is used to sort an array based on frequency
# Taking input from the user for the array
nums = list(map(int, input('Enter space separated numbers: ').split()))

# Declaring a hashmap / dictionary to store the frequencies
freq_map = dict()

# Getting the frequencies of elements into the hashmap
for i in nums:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1

# Defining a function to sort the array in a custom manner
def custom_sort(n):
    return [freq_map[n], -n]

# Sorting the array using the custom sort and built-in sort
nums.sort(key=custom_sort, reverse=True)

# Printing the output
print(nums)