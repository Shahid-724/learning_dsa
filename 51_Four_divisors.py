class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        
        def divisor_sum(n):
            sum = 0
            count = 0
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    sum += i + (n // i)
                    count += 2 if i != n // i else 1
            if count == 4:
                return sum
            return 0

        res = 0
        for i in nums:
            res += divisor_sum(i)

        return res
    
# Time - O(N * SqrtN)
# Space - O(1)