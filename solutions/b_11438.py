import sys
import threading
import math
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(sys.stdin.readline())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    LOG = int(math.log2(N)) + 1
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    up = [[0] * LOG for _ in range(N + 1)]

    def dfs(u, p):
        parent[u] = p
        depth[u] = depth[p] + 1
        up[u][0] = p
        for i in range(1, LOG):
            up[u][i] = up[up[u][i-1]][i-1]
        for v in adj[u]:
            if v != p:
                dfs(v, u)

    dfs(1, 0)

    M = int(sys.stdin.readline())
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if depth[a] < depth[b]:
            a, b = b, a
        # Lift node a to the depth of b
        for i in range(LOG - 1, -1, -1):
            if depth[a] - depth[b] >= (1 << i):
                a = up[a][i]
        if a == b:
            print(a)
            continue
        for i in range(LOG -1, -1, -1):
            if up[a][i] != up[b][i]:
                a = up[a][i]
                b = up[b][i]
        print(up[a][0])

threading.Thread(target=main).start()
