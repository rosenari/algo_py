N = int(input())
letters = list(map(int, input().split()))
numbers = [number for number in range(1, N + 1)]
answer = []
index = 0

while len(letters) > 0: # n
    letter = letters.pop(index) # n
    answer.append(numbers.pop(index))
    index += letter - 1 if letter > 0 else letter
    index = len(letters) + index if index < 0 else index
    index = index % len(letters) if len(letters) > 0 else index

print(*answer)