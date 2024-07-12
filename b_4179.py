import sys


dr = [1, 0, -1, 0]
dc = [0 , -1, 0, 1]
def bfs():
    while len(queue) > 0:
        name, r, c, cnt = queue.pop(0)
        if name == 'J' and (r == 0 or c == 0 or r == R - 1 or c == C - 1):
            if matrix[r][c] == "#":
                continue

            return cnt + 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if name == 'J':
                    if matrix[nr][nc] != "#" and matrix[nr][nc] != "J":
                        matrix[nr][nc] = 'J'
                        queue.append((name, nr, nc, cnt + 1))
                else:
                    if matrix[nr][nc] != "#":
                        matrix[nr][nc] = '#'
                        queue.append((name, nr, nc, cnt + 1))

    return 'IMPOSSIBLE'



input = sys.stdin.readline
R, C = map(int, input().rstrip().split())

matrix = [list(input().rstrip()) for _ in range(R)]
jqueue = []
fqueue = []
for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'J':
            jqueue.append(('J', r, c, 0))
            matrix[r][c] = 'J'
        elif matrix[r][c] == 'F':
            fqueue.append(('F', r, c, 0))
            matrix[r][c] = '#'

queue = jqueue + fqueue

print(bfs())
