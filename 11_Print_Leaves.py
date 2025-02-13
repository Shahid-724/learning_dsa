# This code is used to print all the leaf nodes of a binary tree recursively
# Defining a class TreeNode to create the nodes of a binary tree
class TreeNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

# Creating a few nodes to make a binary tree
a = TreeNode(0)
b = TreeNode(2)
c = TreeNode(4)
d = TreeNode(6)
e = TreeNode(8)
f = TreeNode(10)
g = TreeNode(12)
h = TreeNode(14)
i = TreeNode(16)
j = TreeNode(18)
k = TreeNode(20)

# Connecting the nodes to form a binary tree
root = f
f.left = d
f.right = h
d.left = b
d.right = e
b.left = a
b.right = c
h.left = g
h.right = j
j.left = i
j.right = k

# Defining a function to print the binary tree recursively in order
def print_ll(root):
    if not root:
        return root
    print_ll(root.left)
    print(root.data, end=' ')
    print_ll(root.right)

# Defining a recursive function to print the leaf nodes of a binary tree
def print_leaves(root):
    
    # The case where there is no root
    if not root:
        return

    # The base case
    if not root.left and not root.right:
        print(root.data, end=' ')
        return
    
    # The two recursive calls
    if root.left:
        print_leaves(root.left)
    if root.right:
        print_leaves(root.right)

# Calling the function to print the leaves of a binary tree
print_leaves(root)

# Calling the function to print the binary tree
# print_ll(root)