class Solution:
    def maxProduct(self, nums) -> int:
        
        nums.sort()

        return (nums[-1] - 1) * (nums[-2] - 1)

# Time - O(N logN)
# Space - O(1)