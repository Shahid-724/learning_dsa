# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

class Solution:
    def getTargetCopy(self, original, cloned, target):
        self.res = None
        def dfs(root):
            if not root:
                return None
            if target.val == root.val:
                self.res = root
                return None
            dfs(root.left)
            dfs(root.right)
        dfs(cloned)
        return self.res
    
# Time - O(N)
# Space - O(logN)