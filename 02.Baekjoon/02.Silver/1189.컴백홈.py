# 처음 시작하는 부분 방문 체크 꼭 해야함
# 시작과 끝을 잘 보기

import sys
sys.stdin = open('input.txt', 'r')

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
R, C, K = map(int, input().split())
boards = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ans = 0

def backtrack(r, c, cnt):
    global ans

    if r == 0 and c == C - 1:
        if cnt == K:
            ans += 1
        return
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if visited[nr][nc] or boards[nr][nc] == 'T':
            continue
        visited[nr][nc] = True
        backtrack(nr, nc, cnt + 1)
        visited[nr][nc] = False

visited[R - 1][0] = True
backtrack(R - 1, 0, 1)
print(ans)
