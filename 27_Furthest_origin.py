class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        left = 0
        right = 0
        empty = 0

        for i in moves:
            if i == 'L':
                left += 1
            elif i == 'R':
                right += 1
            else:
                empty += 1

        if left > right:
            return empty + left - right
        return empty + right - left
    
    # Time - O(N)
    # Space - O(1)