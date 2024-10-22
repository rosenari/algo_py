def ccw(a, b):
    result = a[0] * b[1] - a[1] * b[0]
    return int(result if result == 0 else result / abs(result))


p = [list(map(int, input().split())) for _ in range(3)]
vector = [[p[i + 1][0] - p[i][0], p[i + 1][1] - p[i][1]] for i in range(2)]
print(ccw(vector[0], vector[1]))