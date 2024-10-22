N, T = map(int, input().split())
bucket = [0] * N

for s, e, n in [map(int, input().split()) for _ in range(T)]:
    bucket[s - 1:e] = [n] * (e - s + 1)

print(*bucket)