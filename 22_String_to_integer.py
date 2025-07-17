class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Declaring variables
        res = 0
        ptr = 0
        sign = 1
        sign_found = False
        n = len(s)

        # The leading whitespaces
        while ptr < n and s[ptr] == ' ':
            ptr += 1

        # Checking the negative sign
        if ptr < n and s[ptr] == '-':
            sign = -1
            sign_found = True
            ptr += 1

        # Checking the positive sign
        if ptr < n and s[ptr] == '+' and not sign_found:
            ptr += 1

        # Skipping the leading zeroes
        while ptr < n and s[ptr] == '0':
            ptr += 1

        # Reading the digits until a non-digit character
        while ptr < n and s[ptr].isdigit():
            res = res * 10 + int(s[ptr])
            ptr += 1

        # Rounding the result
        res *= sign
        round = 1 << 31
        if res < 0:
            return max(-round, res)
        return min(round - 1, res)
    
# Time - O(N)
# Space - O(1)