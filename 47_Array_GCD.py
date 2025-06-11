class Solution:
    def findGCD(self, nums: list[int]) -> int:
        
        s = float('inf')
        l = float('-inf')

        for i in nums:
            s = min(i, s)
            l = max(i, l)

        while l:
            s, l = l, s % l

        return s
    
# Time - O(N + logM)
# Space - O(1)