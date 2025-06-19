class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        sum = 0
        prod = 1

        while n:
            d = n % 10
            sum += d
            prod *= d
            n //= 10

        return prod - sum
    
# Time - O(logN)
# Space - O(1)