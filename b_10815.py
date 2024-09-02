N = int(input())
numbers = set(input().split())
M = int(input())
print(*[1 if n in numbers else 0 for n in input().split()])
