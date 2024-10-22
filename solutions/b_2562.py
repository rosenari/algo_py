numbers = [int(input()) for _ in range(9)]
m = max(numbers)
print(m)
print(numbers.index(m) + 1)