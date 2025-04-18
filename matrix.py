nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]

m = len(nums)
n = len(nums[0])

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

res = float('-inf')

for i in range(m):
    for j in range(n):
        if i == j or i + j == m - 1:
            if is_prime(nums[i][j]):
                res = max(res, nums[i][j])

print(res)