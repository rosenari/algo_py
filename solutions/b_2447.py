# 2447 별찍기 - 10

def remove_star(sr, sc, size):
    for r in range(sr, sr + size):
        for c in range(sc, sc + size):
            matrix[r][c] = ' '

def star(sr, sc, size):
    m_size = size // 3
    mr = sr + (size // 3)
    mc = sc + (size // 3)
    remove_star(mr, mc, m_size)

    if size == 3:
        return

    [star(sr + (i * m_size), sc + (j * m_size), m_size) for i in range(3) for j in range(3) if not (i == 1 and j == 1)]


N = int(input())
matrix = [['*'] * N for _ in range(N)]
star(0, 0, N)

print('\n'.join([''.join(m) for m in matrix]))