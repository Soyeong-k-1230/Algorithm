# 모든 경우를 확인해봐야한다. Bruteforce

import sys
sys.stdin = open('input.txt', 'r')

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
board = [list(input().split()) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
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
                        if board[nr - dr][nc - dc] == 'T':
                            print('NO')
                            exit()
                        cnt += 1
                        board[i + dr][j + dc] = 'O'
                        break

for i in range(N):
    print(board[i])

if cnt <= 3:
    print('YES')
else:
    print('NO')
