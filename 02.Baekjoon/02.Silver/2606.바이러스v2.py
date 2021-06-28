import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
E = int(input())
nodes = [[] for _ in range(N)]
visited = [False] * N
cnt = 0
for _ in range(E):
    s, e = map(int, input().split())
    nodes[s - 1].append(e - 1)
    nodes[e - 1].append(s - 1)

def dfs(v):
    global cnt
    visited[v] = True
    for w in nodes[v]:
        if not visited[w]:
            cnt += 1
            dfs(w)

dfs(0)
print(cnt)
