import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return (i, j)

def bfs(sr, sc):
    queue = deque()
    queue.append([sr, sc])
    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True

    while queue:
        r, c = queue.popleft()
        if maze[r][c] == 3:
            return 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if visited[nr][nc] or maze[nr][nc] == 1:
                continue
            visited[nr][nc] = True
            queue.append([nr, nc])
    return 0

for _ in range(1, 11):
    tc = int(input())
    N = 16
    maze = [list(map(int, list(input()))) for _ in range(N)]
    start = find_start()
    ans = bfs(start[0], start[1])
    print('#{} {}'.format(tc, ans))
