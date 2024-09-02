import sys

r = sys.stdin.readline
r()
numbers = sorted(list(map(int, r().split())))
print(numbers[0], numbers[-1])