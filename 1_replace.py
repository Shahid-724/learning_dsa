# This code is used to replace an element with its index in a list

# This kind of seems similar to leetcode ques 1920 - Form array from permutation

# def replace(nums):
#     l = len(nums)
#     for i in range(l):
#         nums[i] += l * (nums[nums[i]] % l)
#     for i in range(l):
#         nums[i] //= l
#     return nums

# nums = list(map(int, input('Enter space separated nums: ').split()))
# print(replace(nums))

# No it's not similar to that X

# The question in detail
# - Look at each value and index 
# - Get the index, find the index in the list
# - Append the index of that index from the list to the result

# Approach
# - I think using a hashmap would be good
# - The time complexity must be less that O(n)
# - Hashmap will make the space complexity to be O(n)

def replace2(nums):
    hashmap = dict()
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    result = []
    for i in range(len(nums)):
        result.append(hashmap[i])
    return result

nums = list(map(int, input('Enter space separated nums: ').split()))
print(replace2(nums))

# Done
# Time - O(n)
# Space - O(n)