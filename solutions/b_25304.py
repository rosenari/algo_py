X = int(input())
T = int(input())
print('Yes' if X == sum([price * n for price, n in [map(int, input().split()) for _ in range(T)]]) else 'No')