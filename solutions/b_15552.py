import sys

read = sys.stdin.readline
T = int(read().rstrip())

for _ in range(T):
    a, b = map(int, read().split())
    print(a + b)
