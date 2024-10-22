import sys, heapq

read = sys.stdin.readline
N = int(read())
heap = []

for _ in range(N):
    n = int(read())
    print(0 if len(heap) == 0 else heapq.heappop(heap)) if n == 0 else heapq.heappush(heap, n)