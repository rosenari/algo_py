def traverse(node, store, order='pre'):
    left = tree[node][0]
    right = tree[node][1]

    if order == 'pre':
        store.append(node)

    if left >= 0:
        traverse(left, store, order)

    if order == 'in':
        store.append(node)

    if right >= 0:
        traverse(right, store, order)

    if order == 'post':
        store.append(node)


N = int(input())
tree = [[]] * 26
for _ in range(N):
    n, l, r = map(str, input().split())
    tree[ord(n) - 65] = [ord(l) - 65, ord(r) - 65]

answer = [[], [], []]
traverse(0, answer[0], order='pre')
traverse(0, answer[1], order='in')
traverse(0, answer[2], order='post')

print('\n'.join(''.join(chr(v + 65) for v in a) for a in answer))