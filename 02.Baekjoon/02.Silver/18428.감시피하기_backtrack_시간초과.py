# 실제 조합 함수 만들어서 하면 시간초과

import sys
sys.stdin = open('input.txt', 'r')

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

def check(p):

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

def backtrack(n, s, p):
    if n == 3:

        for n in range(len(p)):
            r = obs[p[n]][0]
            c = obs[p[n]][1]
            board[r][c] = 'O'

        if check(p):
            print('YES')
            exit()

        for n in range(len(p)):
            r = obs[p[n]][0]
            c = obs[p[n]][1]
            board[r][c] = 'X'

    for k in range(s, len(obs)):
        backtrack(n + 1, k + 1, p + [k])

backtrack(0, 0, [])

print('NO')



