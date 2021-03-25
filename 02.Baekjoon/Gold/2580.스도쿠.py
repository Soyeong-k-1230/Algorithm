import sys
sys.stdin = open('input.txt', 'r')
N = 9
board = [list(map(int, input().split())) for _ in range(N)]

def check(r, c, target):
    # 가로
    if target in board[r]:
        return False
    # 세로
    for i in range(N):
        if target == board[i][c]:
            return False
    # 정사각형
    sr, sc = (r // 3) * 3, (c // 3) * 3
    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if target == board[i][j]:
                return False
    return True

def backtrack(n):
    if n == M:
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
        sys.exit(0)
    r, c = zero[n][0], zero[n][1]
    for num in range(1, 10):
        if check(r, c, num):
            board[r][c] = num
            backtrack(n + 1)
            board[r][c] = 0

zero = [(i, j) for i in range(N) for j in range(N) if not board[i][j]]
M = len(zero)
backtrack(0)
