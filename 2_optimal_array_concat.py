def solve(N, a, M, b):
    ma = 0
    mb = 0
    ca = 0
    cb = 0
    for i in range(N):
        ca += a[i]
        if ca > ma:
            ma = ca
        if ca < 0:
            ca = 0
    for i in range(M):
        cb = b[i]
        if cb > mb:
            mb = cb
        if cb < 0:
            cb = 0
    return ma + mb