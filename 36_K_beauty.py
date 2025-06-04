class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        n = str(num)
        res = 0

        for i in range(len(n) - k + 1):
            temp = n[i:i + k]
            if int(temp) and num % int(temp) == 0:
                res += 1

        return res
    
# Time - O(N * K)
# Space - O(1)