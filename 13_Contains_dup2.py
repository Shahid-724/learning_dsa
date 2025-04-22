class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        # Declaring variables
        hashmap = dict()

        # Iterating over nums
        for i in range(len(nums)):
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                return True
            hashmap[nums[i]] = i

        return False
    
# Time - O(N)
# Space - O(N)