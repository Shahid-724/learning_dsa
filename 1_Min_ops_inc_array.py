class Solution:
    def minOperations(self, nums) -> int:
        
        # Declaring variables
        res = 0

        # Iterating the list
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1

        # Returning the result
        return res

# Time - O(N)
# Space - O(1)