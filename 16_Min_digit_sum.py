class Solution:
    def minElement(self, nums: list[int]) -> int:
        
        # Defining a function to calc digit sum
        def digit_sum(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res

        # Declaring variables
        res = float('inf')

        # Iterating over nums
        for i in nums:
            res = min(res, digit_sum(i))

        # Returning the result
        return res
    
# Time - O(N logN)
# Space - O(1)