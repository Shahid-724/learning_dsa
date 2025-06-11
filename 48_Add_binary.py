class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = int(a, 2)
        b = int(b, 2)

        while b:

            without_carry = a ^ b
            carry = a & b
            carry <<= 1

            a = without_carry
            b = carry

        return bin(a)[2:]
    
# Time - O(max(M, N))
# Space - O(1)