class Solution:
    def maxProductDifference(self, nums) -> int:

        # Sorting input
        nums.sort()

        # Calculating and returning the result
        return nums[-1] * nums[-2] - nums[0] * nums[1]
    
# Time - O(N logN)
# Space - O(1)