from collections import deque
def fun(st, n, ad):
    dis = [-1] * (n + 1)
    dis[st] = 0
    x = deque([st])
    while x:
        nod = x.popleft()
        for i in ad[nod]:
            if dis[i] == -1:
                dis[i] = dis[nod] + 1
                x.append(i)
    return dis

def solve(N, K, special_nodes, node_from, node_to):
    ad = [[] for i in range(N + 1)]
    for i in range(len(node_from)):
        u = node_from[i]
        v = node_to[i]
        ad[u].append(v)
        ad[v].append(u)
    x = fun(1, N, ad)
    y = fun(N, N, ad)
    mx = float('inf')
    my = float('inf')
    for i in special_nodes:
        mx = min(mx, x[i])
        my = min(my, y[i])
    md = x[N]
    for i in special_nodes:
        nd = mx + 1 + y[i]
        md = min(md, nd)
    return md