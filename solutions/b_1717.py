import sys
read = sys.stdin.readline

def find(x):
    if p[x] == x:
        return x

    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)

    if rank[x] < rank[y]:
        x, y = y, x

    p[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1

n, m = map(int, read().split())
p = [i for i in range(n + 1)]
rank = [1 for i in range(n + 1)]
for _ in range(m):
    op, a, b = map(int, read().split())
    if op == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')