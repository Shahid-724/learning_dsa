class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        # Declaring variables
        count = 0
        res = 0

        # Iterating over the input
        for i in nums:
            if not count:
                res = i
            count += (1 if res == i else -1)

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(1)