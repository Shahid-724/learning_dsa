class Solution:
    def countDigits(self, num: int) -> int:
        
        temp = num
        res = 0

        while temp:
            d = temp % 10
            if num % d == 0:
                res += 1
            temp //= 10

        return res
    
# Time - O(logN)
# Space - O(1)