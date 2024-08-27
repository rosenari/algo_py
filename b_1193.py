def s_sum(a, num):
    return num * (2 * a + (num - 1) * d)


X = int(input())

ra = 1
ca = 3
d = 4

skip_row = 0
skip_col = 0
for n in range(1, X):
    sr = s_sum(ra, n)
    if sr > X:
        skip_row = n - 1
        break

for n in range(1, X):
    sc = s_sum(ca, n)
    if sc > X:
        skip_col = n - 1
        break
