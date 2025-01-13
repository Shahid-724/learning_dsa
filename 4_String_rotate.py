# This code is used to rotate a string left and right using slicing

def str_rotate(s, k):
    left = s[k:] + s[:k]
    right = s[-k:] + s[:-k]
    return left, right

s = 'geeksforgeeks'
k = 2
print(str_rotate(s, k))

# Time Complexity: O(n)
# Space Complexity: O(n)