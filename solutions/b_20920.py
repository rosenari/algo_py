import sys

read = sys.stdin.readline
N, M = map(int, read().split())
m = {}

for _ in range(N):
    word = read().rstrip()

    if len(word) < M:
        continue

    m[word] = 1 if word not in m else m[word] + 1

print('\n'.join(sorted(m.keys(), key=lambda x: (-m[x], -len(x), x))))
