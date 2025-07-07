class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        # A function to get the numeric value of a string
        def str_to_num(s):

            res = 0
            power = 1

            for i in range(len(s) - 1, -1, -1):
                res += (ord(s[i]) - 97) * power
                power *= 10

            return res

        # Calculating the result
        return str_to_num(firstWord) + str_to_num(secondWord) == str_to_num(targetWord)
    
# Time - O(N)
# Space - O(1)