import sys, heapq

read = sys.stdin.readline
N = int(read())
heap = []

for _ in range(N):
    n = int(read())
    if n != 0:
        heapq.heappush(heap, (-n, n))
    else:
        print(0) if len(heap) == 0 else print(heapq.heappop(heap)[1])