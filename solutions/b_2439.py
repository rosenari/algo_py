N = int(input())
print('\n'.join([f"{' ' * (N - i)}{'*' * i}" for i in range(1, N + 1)]))