# This code is used to count the no. of subarrays with equal no. of 0s and 1s

def equal_zero_ones(nums):
    hashmap = {0: 1}
    prefix_sum = 0
    result = 0
    print(hashmap, prefix_sum, result)
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1
        prefix_sum += nums[i]
        if prefix_sum in hashmap:
            result += hashmap[prefix_sum]
            hashmap[prefix_sum] += 1
        else:
            hashmap[prefix_sum] = 1
        print(hashmap, prefix_sum, result)
    return result

nums = [1,0,0,1,0,1,1]
print(equal_zero_ones(nums))

# Did not understand this perfectly
# Need to do this again