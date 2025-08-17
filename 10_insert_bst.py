# This code is used to insert a node into a binary search tree recursively
# Defining a class TreeNode to create the nodes of a binary tree
class TreeNode:

    # The instance variables
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

# Creating a few nodes to make a binary search tree
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

# Connecting the nodes to form a binary search tree
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

# Defining a function to print the binary search tree recursively in order
def print_bst(root):
    if not root:
        return root
    print_bst(root.left)
    print(root.data, end=' ')
    print_bst(root.right)

# Defining a function to insert a node into a binary search tree recursively
def insert_bst(root, val):
    
    # The base case
    if not root:
        root = TreeNode(val)
        return root
    
    # The recursive calls
    if val < root.data:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

# Asking a value from the user to insert into a binary search tree
n = int(input('Enter a number: '))

# Calling the function to print the binary tree before insertion
print_bst(root)
print()

# Calling the function to insert a node into the binary search tree
new_root = insert_bst(root, n)

# Calling the function to print the binary tree after insertion
print_bst(new_root)