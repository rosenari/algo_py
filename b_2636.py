import sys


dr = [0, 1, 0 ,-1]
dc = [-1, 0, 1 ,0]
def bfs():
    v = [[False for _ in range(C)] for _ in range(R)]
    queue = [(0, 0)]
    while len(queue) != 0:
        r, c = queue.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and v[nr][nc] == False:
                v[nr][nc] = True
                if matrix[nr][nc] == 0:
                    queue.append((nr, nc))
                elif matrix[nr][nc] == 1:
                    matrix[nr][nc] = 0

def get_cheese_cnt():
    return [b for rows in matrix for b in rows].count(1)

input = sys.stdin.readline
R, C = map(int, input().split())

matrix = [list(map(int, input().rstrip().split())) for _ in range(R)]


answer = 0
cheese_cnt = get_cheese_cnt()
prev_cnt = cheese_cnt

while cheese_cnt > 0:
    bfs()
    prev_cnt = cheese_cnt
    cheese_cnt = get_cheese_cnt()
    answer += 1

print(answer)
print(prev_cnt)