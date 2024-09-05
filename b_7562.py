def bfs(start, end, v, s):
    queue = [start + (0,)]

    while len(queue) > 0:
        r, c, cnt = queue.pop(0)

        if (r, c) == end:
            return cnt

        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < s and 0 <= nc < s and v[nr][nc] is False:
                v[nr][nc] = True
                queue.append((nr, nc, cnt+1))


T = int(input())
d = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

for t in range(T):
    N = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    visited = [[False for _ in range(N)] for _ in range(N)]
    print(bfs((sr, sc), (er, ec), visited, N))