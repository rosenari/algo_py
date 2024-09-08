import sys

read = sys.stdin.readline
N = int(read())
m, numbers = {}, []

for _ in range(N):
    number = int(read())
    m[number] = m[number] + 1 if number in m else 1
    numbers.append(number)

numbers = sorted(numbers)
m = sorted(m.items(), key=lambda x: (-x[1], x[0]))
print(round(sum(numbers) / N))
print(numbers[(N // 2)])
print(m[1][0] if len(m) > 1 and m[0][1] == m[1][1] else m[0][0])
print(numbers[len(numbers) - 1] - numbers[0])

