class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        # Declaring variables
        m1 = m2 = m3 = float('-inf')

        # Iterating over nums
        for i in nums:
            if i > m1:
                m1, m2, m3 = i, m1, m2
            elif m1 > i > m2:
                m2, m3 = i, m2
            elif m2 > i > m3:
                m3 = i

        # Checking condition and returning result
        if m3 == float('-inf'):
            return m1
        return m3
    
# Time - O(N)
# Space - O(1)