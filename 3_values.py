# This is a question, it has a linked list
# Prints an array containing all the values of the linked list

# Creating the node class
class Node:

    # The instance variables
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

# Creating the nodes of the linked list
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# Creating the links
a.next = b
b.next = c
c.next = d

# Declaring a list to store the result
result = []

# Traversing the list and storing the elements in the list
def ll_to_array(head):
    cur = head
    while cur is not None:
        result.append(cur.val)
        cur = cur.next

# Calling the function
ll_to_array(a)

# Printing the result
print(result)