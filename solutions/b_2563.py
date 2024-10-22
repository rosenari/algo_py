vector = [0 for _ in range(100 * 100)]
for r, c in [map(int, input().split()) for _ in range(int(input()))]:
    start = r * 100 + c
    for pos in range(start, start + (100 * 10), 100):
        vector[pos:pos+10] = [1] * 10
print(vector.count(1))