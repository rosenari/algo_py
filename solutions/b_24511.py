from collections import deque

N = int(input())
s_type = list(map(int, input().split()))
state = deque(v for i, v in enumerate(map(int, input().split())) if s_type[i] == 0)
M = int(input())
answer = [0] * M

for i, num in enumerate(map(int, input().split())):
    state.appendleft(num)
    answer[i] = state.pop()
print(*answer)
