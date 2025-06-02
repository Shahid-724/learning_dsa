class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        res = 0
        place = 1

        for i in range(4):
            
            temp = float('inf')

            temp = min(temp, num1 % 10)
            num1 //= 10
            temp = min(temp, num2 % 10)
            num2 //= 10
            temp = min(temp, num3 % 10)
            num3 //= 10

            res += temp * place
            place *= 10

        return res
    
# Time - O(1)
# Space - O(1)