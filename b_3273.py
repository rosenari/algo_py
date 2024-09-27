N = int(input())
seq = sorted(list(map(int, input().split())))
X = int(input())

s, e = 0, N - 1
answer = 0

while s < e:
    t = seq[s] + seq[e]
    if t >= X:
        if t == X:
            answer = answer + 1
        e = e - 1
    else:
        s = s + 1

print(answer)
