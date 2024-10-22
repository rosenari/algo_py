import sys

numbers = [int(sys.stdin.readline()) for _ in range(int(input()))]
numbers.sort()
for number in numbers:
    print(number)