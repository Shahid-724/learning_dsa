class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        
        # Declaring variables
        self.res = 0

        # Traversing the tree
        def dfs(root, is_left=False):
            if not root:
                return None
            
            if is_left and not root.left and not root.right:
                self.res += root.val

            dfs(root.left, True)
            dfs(root.right, False)
        
        dfs(root)
        return self.res
        
# Time - O(N)
# Space - O(logN)