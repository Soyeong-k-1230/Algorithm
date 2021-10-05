import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
kit = list(map(int, input().split()))
visited = [False] * N
cnt = 0
def backtrack(n, total):
    global cnt
    if total < 500:
        return
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtrack(n + 1, total + kit[i] - K)
            visited[i] = False

backtrack(0, 500)
print(cnt)
