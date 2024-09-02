import math

def sum_cut(s, e):
    num = trees[s]
    return sum([trees[i] - num for i in range(s, e)])


N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))
answer = 0

start = 0
end = N - 1

while start <= end:
    mid = (start + end) // 2

    total = sum_cut(mid, N)
    if total <= M:
        answer = trees[mid] - math.ceil((M - total)/(N - mid))
        end = mid - 1
    else:
        start = mid + 1

print(answer)