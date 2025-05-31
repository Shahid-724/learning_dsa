class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        
        def digit(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res

        element_sum = 0
        digit_sum = 0

        for i in nums:
            digit_sum += digit(i)
            element_sum += i

        return abs(digit_sum - element_sum)
    
# Time - O(N * K)
# Space - O(1)