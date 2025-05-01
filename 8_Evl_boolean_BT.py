# You need to learn the iterative version of this !!!

class Solution:
    def evaluateTree(self, root) -> bool:

        # The base case
        if not root.left and not root.right:
            return root.val == 1
        
        # Traversing the left and right subtrees
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)

        # Returning the boolean operation between l and r
        if root.val == 3:
            return l and r == 1
        return l or r == 1
    
# Time - O(N)
# Space - O(N)