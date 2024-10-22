N = int(input())
numbers = list(map(int, input().split()))
sorted_number = sorted(set(numbers))
m = {v:i for i, v in enumerate(sorted_number)}
print(*[m[n] for n in list(numbers)])
