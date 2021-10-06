# 시간초과, 5%에서 멈춤

# backtrack 사용 X, 재귀
import sys
sys.stdin = open('input.txt', 'r')

dirs = [[(0, -1), (1, 0)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0

def search(total):
    global ans
    print()
    ans = max(ans, total)

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                for w in dirs:

                    if i + w[0][0] < 0 or i + w[1][0] < 0:
                        continue
                    if i + w[0][0] >= N or i + w[1][0] >= N:
                        continue
                    if j + w[0][1] < 0 or j + w[1][1] < 0:
                        continue
                    if j + w[0][1] >= M or j + w[1][1] >= M:
                        continue
                    if visited[i + w[0][0]][j + w[0][1]]:
                        continue
                    if visited[i + w[1][0]][j + w[1][1]]:
                        continue

                    visited[i + w[0][0]][j + w[0][1]] = True
                    visited[i + w[1][0]][j + w[1][1]] = True
                    visited[i][j] = True
                    for k in range(N):
                        print(visited[k])
                    print()
                    print(i, j)
                    tmp = board[i + w[0][0]][j + w[0][1]] + board[i + w[1][0]][j + w[1][1]]
                    search(total + board[i][j] * 2 + tmp)
                    visited[i + w[0][0]][j + w[0][1]] = False
                    visited[i + w[1][0]][j + w[1][1]] = False
                    visited[i][j] = False

search(0)
print(ans)
