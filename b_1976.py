import sys


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


read = sys.stdin.readline

N, M = int(read()), int(read())
p = [n for n in range(0, N + 1)]
rank = [1] * (N + 1)

for i in range(N):
    for j, v in enumerate(map(int, read().split())):
        if i != j and v == 1:
            union(i + 1, j + 1)

plan = list(map(int, read().split()))
for s, e in [(plan[n - 1], plan[n]) for n in range(1, len(plan))]:
    if find(s) != find(e):
        print('NO')
        exit()

print('YES')