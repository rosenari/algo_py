def bfs():
    queue = [(0, 0, 1)]

    while len(queue) > 0:
        r, c, cnt = queue.pop(0)
        if r == N -1 and c == M - 1:
            return cnt

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if matrix[nr][nc] == 0 or v[nr][nc]:
                continue

            queue.append((nr, nc, cnt + 1))
            v[nr][nc] = True



N, M  = map(int, input().split())
v = [[False] * M for _ in range(N)]
matrix = [[int(c) for c in input()] for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

print(bfs())