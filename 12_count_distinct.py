# This code is used to count the distinct elements in an array
# Taking input for array from the user
nums = list(map(int, input('Enter space separated numbers: ').split()))

# Using a set to store the distinct elements
distinct_elements = set()

# Adding elements to the set
for i in nums:
    if i not in distinct_elements:
        distinct_elements.add(i)

# Printing the length of the set to get count the distinct elements
print(f'The no. of distinct element is {len(distinct_elements)}')