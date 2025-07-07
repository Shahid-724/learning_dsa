class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        max_zeroes = 0
        cur_zeroes = 0
        max_ones = 0
        cur_ones = 0

        for i in s:
        
            if i != '0':
                max_zeroes = max(max_zeroes, cur_zeroes)
                cur_zeroes = 0
            else:
                cur_zeroes += 1

            if i != '1':
                max_ones = max(max_ones, cur_ones)
                cur_ones = 0
            else:
                cur_ones += 1

        max_zeroes = max(max_zeroes, cur_zeroes)
        max_ones = max(max_ones, cur_ones)

        return max_ones > max_zeroes
    
# Time - O(N)
# Space - O(1)