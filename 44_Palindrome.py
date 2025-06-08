class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        div = 1
        while div * 10 < x:
            div *= 10

        while x:
            if x % 10 != x // div:
                return False
            x = (x % div) // 10
            div //= 100

        return True
    
# Time - O(logN)
# Space - O(1)