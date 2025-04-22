class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        actual = sum(nums)
        return total - actual
    
# Time - O(N)
# Space - O(1)