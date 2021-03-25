import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

def bfs(sr, sc):
    queue = deque()
    queue.append((sr, sc, 0, 1))
    visited_origin = [[False] * M for _ in range(N)]
    visited_crack = [[False] * M for _ in range(N)]
    visited_origin[sr][sc] = True
    ans_list = []

    while queue:
        r, c, crack, cnt = queue.popleft()
        if r == (N - 1) and c == (M - 1):
            # ans_list.append(cnt)
            return cnt
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if crack == 0 and visited_origin[nr][nc]:
                continue
            if crack == 1 and visited_crack[nr][nc]:
                continue
            if board[nr][nc] == 1 and crack == 0:
                visited_crack[nr][nc] = True
                queue.append((nr, nc, 1, cnt + 1))
            if not board[nr][nc]:
                if crack == 0:
                    visited_origin[nr][nc] = True
                if crack == 1:
                    visited_crack[nr][nc] = True
                queue.append((nr, nc, crack, cnt + 1))

    return -1
    # return ans_list

ans = bfs(0, 0)
print(ans)
# if not len(ans):
#     print(-1)
# else:
#     print(min(ans))
