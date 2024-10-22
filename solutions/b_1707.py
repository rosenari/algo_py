import sys
from collections import deque

read = sys.stdin.readline


def bfs(node, color):
    queue = deque([(node, color)])
    colors[node] = color

    while queue:
        n, c = queue.popleft()

        nc = c * -1
        for nn in graph[n]:
            if colors[nn] == c:
                return False

            if colors[nn] == 0:
                colors[nn] = nc
                queue.append((nn, nc))

    return True


K = int(read())

for _ in range(K):
    V, E = map(int, read().split())
    graph = [[] for _ in range(V)]
    colors = [0] * V
    for _ in range(E):
        u, v = map(int, read().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    answer = 'YES'
    for i in range(V):
        if colors[i] == 0 and bfs(i, 1) is False:
            answer = 'NO'

    print(answer)


