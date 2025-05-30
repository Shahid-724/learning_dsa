class Solution:
    def isUgly(self, n: int) -> bool:

        if not n:
            return False

        while n % 2 == 0:
            n //= 2

        while n % 3 == 0:
            n //= 3

        while n % 5 == 0:
            n //= 5

        return n == 1
    
# Time - O(logN)
# Space - O(1)