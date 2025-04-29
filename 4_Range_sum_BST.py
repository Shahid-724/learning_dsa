class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        self.total = 0
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            if root.val >= low and root.val <= high:
                self.total += root.val
            dfs(root.right)
        dfs(root)
        return self.total
    
# Time - O(N)
# Space - O(logN)


class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
    
# This has the same time and space complexities but it is a bit more optimized