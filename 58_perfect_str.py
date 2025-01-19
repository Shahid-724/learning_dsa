from collections import Counter

def solve(n, s, t):
    # Check if lengths are equal
    if len(s) != len(t):
        return False
    
    # Count the frequency of characters in both strings
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Check if both dictionaries are equal
    if count_s == count_t:
        return True
    else:
        return False

print(solve(3, 'baa', 'bcc'))

# Netcore Question