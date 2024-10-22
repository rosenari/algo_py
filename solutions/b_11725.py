import sys
from collections import deque


def bfs():
    queue = deque([1])
    while len(queue) > 0:
        n = queue.popleft()
        for ln in path_list[n]:
            if v[ln] is False:
                p[ln] = n
                v[ln] = True
                queue.append(ln)
    return p[2:]


read = sys.stdin.readline
N = int(read())
path_list = [set() for _ in range(N + 1)]
p = [1] * (N + 1)
v = [False] * (N + 1)

for _ in range(N - 1):
    s, e = map(int, read().split())
    path_list[s].add(e)
    path_list[e].add(s)

print(*bfs(), sep='\n')
