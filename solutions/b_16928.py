def bfs():
    queue = [(1 , 0)]

    while len(queue) > 0:
        n, cnt = queue.pop(0)
        if n == 100:
            return cnt

        for j in range(1, 7):
            if n + j <= 100 and v[n + j] is False:
                nn = portal[n + j] if portal[n + j] != 0 else n + j
                queue.append((nn, cnt + 1))
                v[nn] = True


N, M = map(int, input().split())
portal = [0] * 101
v = [False] * 101

for _ in range(N + M):
    i, t = map(int, input().split())
    portal[i] = t

print(bfs())