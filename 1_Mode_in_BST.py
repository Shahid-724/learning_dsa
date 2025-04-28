# Using a hashmap

def findMode(root):
    
    # Declaring variables
    hashmap = dict()
    res = []
    max_freq = 0

    # Traversing the tree
    def dfs(root):
        if not root:
            return None
        hashmap[root.val] = 1 + hashmap.get(root.val, 0)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    
    # Getting the mode
    for i in hashmap:
        if hashmap[i] > max_freq:
            max_freq = hashmap[i]

    for i in hashmap:
        if hashmap[i] == max_freq:
            res.append(i)

    return res

# Time - O(N)
# Space - O(N)

# Without Hashmap
class Solution:
    def findMode(self, root):
        # Declaring variables
        res = []       # To store the result of the modes
        self.prev = None  # Keeps track of the previous node's value
        self.count = 0     # Count of occurrences of the current value
        self.max_val = 0   # Tracks the maximum frequency of any value
        
        # Helper function for in-order traversal
        def dfs(root):
            if not root:
                return
            
            # Traverse left subtree
            dfs(root.left)
            
            # Process the current node
            if self.prev is None or self.prev != root.val:
                self.count = 1  # Reset count if we encounter a new value
            else:
                self.count += 1  # Increment count if same as previous value
            
            # Check if we found a new mode or if the count equals the max_val
            if self.count > self.max_val:
                self.max_val = self.count
                res.clear()  # Clear previous results as we found a new higher frequency
                res.append(root.val)
            elif self.count == self.max_val:
                res.append(root.val)  # Add the current value to the result if it matches the max frequency
            
            # Update prev to the current node's value
            self.prev = root.val
            
            # Traverse right subtree
            dfs(root.right)
        
        # Start the DFS traversal from the root
        dfs(root)
        
        return res
