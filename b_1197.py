import sys


def find(x):
    if p[x] == x:
        return x

    p[x] = find(p[x])
    return p[x]


def union(x, y):
    x, y = find(x), find(y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        x, y = y, x

    p[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1

    return True


read = sys.stdin.readline
V, E = map(int, read().split())

edges = sorted([tuple(map(int, read().split())) for _ in range(E)], key=lambda x: x[2])
p = [i for i in range(V + 1)]
rank = [1 for i in range(V + 1)]
weights = []

for v1, v2, w in edges:
    if union(v1, v2) is True:
        weights.append(w)

    if len(weights) == V - 1:
        print(sum(weights))
        exit()