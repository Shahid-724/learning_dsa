class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        
        # Declaring variables
        res = TreeNode()
        self.temp = res

        # Traversing the input tree using inorder traversal
        def dfs(root):
            if not root:
                return None

            dfs(root.left)

            new_node = TreeNode(root.val)
            self.temp.right = new_node
            self.temp = self.temp.right

            dfs(root.right)
        dfs(root)

        return res.right
    
# Time - O(N)
# Space - O(logN)