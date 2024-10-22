T = int(input())
print('\n'.join([str(sum(map(int, input().split()))) for i in range(T)]))