class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        def dec_to_bin(num):
            binary = 0
            place = 1
            while num:
                d = num % 2
                binary += d * place
                num //= 2
                place *= 10
            return binary

        res = ''
        date_parts = date.split('-')

        for i in date_parts:
            temp = dec_to_bin(int(i))
            res += str(temp) + '-'

        return res[:-1]
    
# Time - O(N)
# Space - O(1)