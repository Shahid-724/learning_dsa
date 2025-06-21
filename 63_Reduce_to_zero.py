class Solution:
    def numberOfSteps(self, num: int) -> int:

        if not num:
            return num
        
        bit_length = 0
        one_bits = 0

        while num:
            d = num % 2
            if d:
                one_bits += 1
            bit_length += 1
            num //= 2

        return bit_length + one_bits - 1
    
# Time - O(logN)
# Space - O(1)