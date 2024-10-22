wl, hl = [[0, r] for r in map(int, input().split())]

for _ in range(int(input())):
    d, pos = map(int, input().split())
    if d == 0:
        hl.append(pos)
    else:
        wl.append(pos)

wl.sort()
hl.sort()
wl = [wl[i] - wl[i-1] for i in range(1, len(wl))]
hl = [hl[i] - hl[i-1] for i in range(1, len(hl))]

print(max(wl) * max(hl))