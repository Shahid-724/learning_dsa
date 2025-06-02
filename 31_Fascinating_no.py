class Solution:
    def isFascinating(self, n: int) -> bool:
        
        def get_digits(n):
            while n:
                d = n % 10
                if d:
                    if d not in hashset:
                        hashset.add(d)
                    else:
                        return False
                n //= 10
            return True

        hashset = set()

        r1 = get_digits(n)
        r2 = get_digits(2 * n)
        r3 = get_digits(3 * n)

        print(hashset)

        return r1 and r2 and r3 and len(hashset) == 9
    
# Time - O(logN)
# Space - O(1)