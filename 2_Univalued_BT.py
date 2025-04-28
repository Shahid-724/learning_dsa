class Solution:
    def isUnivalTree(self, root):
        
        # Declaring variables
        self.val = root.val

        # Traversing the tree
        def dfs(root):
            if not root:
                return True

            if self.val != root.val:
                return False

            l = dfs(root.left)
            r = dfs(root.right)

            return l and r

        return dfs(root)
    
# Time - O(N)
# Space - O(logN)