N = int(input())
a, b, c = 1, 2, N
for i in range(2, N):
    c = (a + b) % 15746
    a, b = b, c

print(c)