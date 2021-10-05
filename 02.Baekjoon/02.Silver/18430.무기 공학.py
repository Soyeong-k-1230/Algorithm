import sys
sys.stdin = open('input.txt', 'r')

dirs = [[(0, -1), (1, 0)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def backtrack(r, c):
    if r == N and c == M:
        return

print(visited)

