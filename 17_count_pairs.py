# This code is used to count the no. of pairs with the given sum

def count_pairs(nums, target):
    count = 0
    hashmap = dict()
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            count += hashmap[target - nums[i]]
        if nums[i] in hashmap:
            hashmap[nums[i]] += 1
        else:
            hashmap[nums[i]] = 1
    return count

nums = [10, 12, 10, 15, -1]
target = 125
print(count_pairs(nums, target))