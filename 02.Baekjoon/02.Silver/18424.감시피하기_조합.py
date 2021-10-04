# itertools의 combinations 사용하면 시간 통과

import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
board = [list(input().split()) for _ in range(N)]
cnt = 0
obs = []
teachers = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            obs.append((i, j))
        if board[i][j] == 'T':
            teachers.append((i, j))

def check():
    for i, j in teachers:
        for dr, dc in dirs:
            nr, nc = i, j
            while True:
                nr += dr
                nc += dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                if board[nr][nc] == 'O':
                    break
                if board[nr][nc] == 'X':
                    continue
                if board[nr][nc] == 'S':
                    return False
    return True


for blank in list(combinations(obs, 3)):
    for r, c in blank:
        board[r][c] = 'O'

    if check():
        print('YES')
        exit()

    for r, c in blank:
        board[r][c] = 'X'

print('NO')
