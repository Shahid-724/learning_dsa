class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        
        def is_non_zero(num):
            while num:
                d = num % 10
                if not d:
                    return False
                num //= 10
            return True

        for i in range(1, (n // 2) + 1):
            if is_non_zero(i) and is_non_zero(n - i):
                return [i, n - i]
            
# Time - O(N logN)
# Space - O(1)