def chk_row(r, num):
    return num not in sudoku[r]

def chk_col(c, num):
    return len([num for r in range(N) if sudoku[r][c] == num]) == 0

def chk_box(r, c, num):
    box_r = r // 3 * 3
    box_c = c // 3 * 3
    return len([num for i in range(box_r, box_r + 3) for j in range(box_c, box_c + 3) if sudoku[i][j] == num]) == 0

N = 9
sudoku = [list(map(int, input().split())) for i in range(N)]
zero_pos = [(r, c) for r in range(N) for c in range(N) if sudoku[r][c] == 0]

def dfs(index):
    if index == len(zero_pos):
        [print(*s) for s in sudoku]
        exit()

    r, c = zero_pos[index]
    for n in range(1, 10):
        if chk_row(r, n) and chk_col(c, n) and chk_box(r, c, n):
            sudoku[r][c] = n
            dfs(index + 1)
            sudoku[r][c] = 0

dfs(0)