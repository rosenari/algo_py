"""
r(n) = a(n+1) / a(n)
a(n+2) = A * a(n+1) + B * a(n)
r(n+1) = A + B / r(n)
lim 적용 => r^2 - A * r - B
근의 공식 => (A +- sqrt(A ^ 2 + 4 * B)) / 2
(A - sqrt(A ^ 2 + 4 * B)) / 2 는 반드시 음수이며,
근이 - 일경우 수열은 진동하게 되므로 (A + sqrt(A ^ 2 + 4 * B)) / 2가 극한값이 된다.
"""
b, c, a1, a2 = map(int, input().split())
print((b + ((b ** 2 + (4 * c)) ** 0.5)) / 2)