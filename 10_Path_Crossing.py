class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        # Declaring variables
        pos = (0, 0)
        hashset = {pos}

        # Iterating the input
        for i in path:

            # Updating the postion
            if i == 'N':
                pos = (pos[0], pos[1] + 1)
            elif i == 'S':
                pos = (pos[0], pos[1] - 1)
            elif i == 'E':
                pos = (pos[0] + 1, pos[1])
            else:
                pos = (pos[0] - 1, pos[1])

            # Checking if the postion is already visited
            if pos in hashset:
                return True

            hashset.add(pos)

        return False
    
# Time - O(N)
# Space - O(N)