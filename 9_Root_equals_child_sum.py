class Solution:
    def checkTree(self, root):
        return root.val == root.left.val + root.right.val
    
# Time - O(1)
# Space - O(1)