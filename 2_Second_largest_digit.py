class Solution:
    def secondHighest(self, s: str) -> int:
        
        # Declaring variables
        m1 = -1
        m2 = -1

        # Iterating over the string
        for i in s:
            if i.isdigit():
                if int(i) > m1:
                    m1, m2 = int(i), m1
                elif m1 > int(i) > m2:
                    m2 = int(i)

        # Returning the result
        return m2
    
# Time - O(N)
# Space - O(1)