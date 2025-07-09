class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        res = ''

        for i in s:
            if i == ' ':
                k -= 1
                if not k:
                    break
            res += i

        return res
    
# Time - O(N)
# Space - O(N)