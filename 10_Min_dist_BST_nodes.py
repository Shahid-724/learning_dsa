def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        # Declaring variables
        self.prev = float('-inf')
        self.res = float('inf')

        # Traversing the tree using inorder traversal
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.res = min(self.res, root.val - self.prev)
            self.prev = root.val
            dfs(root.right)

        # Calling the function and returning the result
        dfs(root)
        return self.res

# Time - O(N)
# Space - O(N)