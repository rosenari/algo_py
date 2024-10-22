import sys, heapq

read = sys.stdin.readline
N = int(read())
heap = []

for _ in range(N):
    num = int(read())
    if num == 0:
        print(heapq.heappop(heap)[1]) if len(heap) > 0 else print(0)
    else:
        heapq.heappush(heap, (abs(num), num))