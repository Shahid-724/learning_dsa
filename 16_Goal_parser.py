class Solution:
    def interpret(self, command: str) -> str:
        
        hashmap = {'()': 'o', '(al)': 'al'}

        res = ''
        l = 0
        r = 0

        while r < len(command):
            if command[l] == 'G':
                res += 'G'
                l += 1
            elif command[l:r + 1] in hashmap:
                res += hashmap[command[l:r + 1]]
                l = r + 1
            r += 1

        return res
    
# Time - O(N)
# Space - O(1)