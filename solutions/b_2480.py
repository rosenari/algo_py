numbers = list(map(int, input().split()))
count = len(set(numbers))
numbers.sort()

if count == 1:
    print(10000 + numbers[0] * 1000)
elif count == 2:
    print(1000 + numbers[1] * 100)
else:
    print(numbers[2] * 100)