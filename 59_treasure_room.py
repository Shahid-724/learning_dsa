def solve(n, tiles):
    dp = [[float('inf')] * n for _ in range(n)]
    print(dp)
    dp[0][0] = count_leading_zeros(tiles[0][0])
    
    for i in range(n):
        for j in range(n):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + count_leading_zeros(tiles[i][j]))
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + count_leading_zeros(tiles[i][j]))
    
    return dp[n-1][n-1]

def count_leading_zeros(num):
    str_num = str(num)
    return len(str_num) - len(str_num.lstrip('0'))

n = 3
tiles = [[2, 3, 10], [5, 10, 3], [4, 2, 5]]

out_ = solve(n, tiles)
print(out_)
