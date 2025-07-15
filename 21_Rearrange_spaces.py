class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        # Counting the spaces and words
        spaces = 0
        words = 0

        for i in range(len(text)):
            if text[i] == ' ':
                spaces += 1
                if i + 1 < len(text) and text[i + 1] != ' ':
                    words += 1

        if text[0] != ' ':
            words += 1

        if words == 1:
            return text.strip() + ' ' * spaces


        # Calculating the spaces in between and end
        spaces_bw = spaces // (words - 1)
        spaces_end = spaces - (words - 1) * spaces_bw

        # Making the result
        res = ''
        ptr = 0

        while ptr < len(text):

            while ptr < len(text) and text[ptr] == ' ':
                ptr += 1

            while ptr < len(text) and text[ptr] != ' ':
                res += text[ptr]
                ptr += 1

            res += ' ' * spaces_bw

        res = res.rstrip()
        res += ' ' * spaces_end

        return res
    
# Time - O(N)
# Space - O(N)

# The space is for result, no extra data structure is used