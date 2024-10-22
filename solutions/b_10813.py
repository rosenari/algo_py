N, T = map(int, input().split())
bucket = [i + 1 for i in range(N)]

for _ in range(T):
    a, b = map(int, input().split())
    bucket[a - 1], bucket[b - 1] = bucket[b - 1], bucket[a - 1]

print(*bucket)