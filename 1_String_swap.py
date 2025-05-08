class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # Declaring variables
        first = 0
        second = 0
        diff = 0

        # Iterating over the strings
        for i in range(len(s1)):

            # We only care about the case where they are not equal
            if s1[i] != s2[i]:
                diff += 1

                # If the diff is greater that 2
                if diff > 2:
                    return False

                # If this is the first difference
                if diff == 1:
                    first = i

                # If this is not the first diff
                else:
                    second = i

        # Checking if the swaps are valid and returning
        return s1[first] == s2[second] and s1[second] == s2[first]
    
# Time - O(N)
# Space - O(1)