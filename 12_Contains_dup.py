class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        # Declaring variables
        hashset = set()

        # Iterating over nums
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False
    
# Time - O(N)
# Space - O(N)