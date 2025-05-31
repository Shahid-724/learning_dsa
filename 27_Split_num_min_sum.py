class Solution:
    def splitNum(self, num: int) -> int:
        
        digits = []
        n1 = 0
        n2 = 0
        place = 1

        while num:
            digits.append(num % 10)
            num //= 10

        digits.sort(reverse=True)

        for i in range(len(digits)):
            if i % 2 == 0:
                n1 += digits[i] * place
            else:
                n2 += digits[i] * place
                place *= 10

        return n1 + n2

# Time - O(N logN)
# Space - O(N)