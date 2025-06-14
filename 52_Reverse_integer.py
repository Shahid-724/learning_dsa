class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        sign = 1

        if x < 0:
            x = abs(x)
            sign = -1

        while x:
            d = x % 10
            rev = rev * 10 + d
            x //= 10

        rev *= sign
        
        round = 1 << 31
        if -round <= rev <= round - 1:
            return rev
        return 0
    
# Time - O(N)
# Space - O(1)