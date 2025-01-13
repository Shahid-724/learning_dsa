# This code is used to get the min no. of rotations to make equal strings

def min_rotations(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1 == s2:
            return count
        s1 = s1[1:] + s1[:1]
        count += 1

s1 = 'geeks'
s2 = 'eeksg'
print(min_rotations(s1, s2))

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)