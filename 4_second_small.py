# # This code is used to find the second smallest element in an array
# # Taking an array as input
# nums = list(map(int, input('Enter space seperated numbers: ').split()))

# # Declaring variables for smallest and second smallest
# smallest = nums[0]
# second_s = nums[0]

# # Iterating through and getting the result
# for i in nums:
#     if i < smallest:
#         smallest = i
#     if i > smallest and i < second_s:
#         second_s = i

# # Printing the result
# print(f'The second smallest is {second_s}')


def second_largest(nums):
    m1 = m2 = float('-inf')
    for i in nums:
        if i > m1:
            m1, m2 = i, m1
        elif m1 > i > m2:
            m2 = i
    return m2

nums = [1, 2, 3, 4, 5]
print(second_largest(nums))