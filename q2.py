def getRelativeRatings(skill, rating, k):
    import heapq
    n = len(skill)
    p = list(enumerate(zip(skill, rating)))
    p.sort(key=lambda x:x[1][0])
    res = [0] * n
    h = []
    s = 0
    for i in range(n):
        si, ri = p[i][1]
        y = p[i][0]
        res[y] = s
        heapq.heappush(h, ri)
        s += ri
        if len(h) > k:
            s = s - heapq.heappop(h)
    return res

skill = list(map(int, input().split()))
rating = list(map(int, input().split()))
k = int(input())
print(getRelativeRatings(skill, rating, k))

# Time Complexity: O(n logn)
# Space Complexity: O(n)