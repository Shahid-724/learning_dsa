class Solution:
    def twoSum(self, nums: list, target: int):
        
        hashmap = dict()

        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap[target - nums[i]]]
            hashmap[nums[i]] = i

# Time - O(N)
# Space - O(N)