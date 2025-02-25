# This code is the same as 3
# This code uses a recursive function

# Creating the node class
class Node:

    # The instance variables
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


# Creating the nodes
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# Creating the links
a.next = b
b.next = c
c.next = d

# Declaring a variable for result
result = []

# Getting the values into the result using a function
def ll_to_array(head):
    if head is None:
        return
    result.append(head.val)
    ll_to_array(head.next)

# Calling the function
ll_to_array(a)

# Printing the result
print(result)
