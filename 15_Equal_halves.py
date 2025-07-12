class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        n = len(s) // 2
        first = 0
        second = 0
        i = 0

        while i < len(s) // 2:
            if s[i].lower() in 'aeiou':
                first += 1
            if s[n].lower() in 'aeiou':
                second += 1
            i += 1
            n += 1

        return first == second
    
# Time - O(N)
# Space - O(1)