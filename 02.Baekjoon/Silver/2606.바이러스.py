import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = True
    for w in node[v]:
        if not visited[w]:
            dfs(w)

N = int(input())
M = int(input())
node = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

visited = [False] * (N + 1)
cnt = 0
dfs(1)
print(cnt - 1)

