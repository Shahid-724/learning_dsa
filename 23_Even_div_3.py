class Solution:
    def averageValue(self, nums: list[int]) -> int:
        
        sum = 0
        count = 0

        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sum += i
                count += 1

        if not count:
            return 0
        return sum // count
    
# Time - O(N)
# Space - O(1)