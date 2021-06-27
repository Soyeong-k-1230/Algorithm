from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
N, M, V = map(int, input().split())

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for w in node[v]:
        if not visited[w]:
            dfs(w)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited = [False] * (N + 1)
    visited[v] = True
    path = []

    while queue:
        n = queue.popleft()
        path.append(n)
        for w in node[n]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
    return path


node = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)
    node[s].sort()
    node[e].sort()

visited = [False] * (N + 1)
dfs(V)
print()
p = bfs(V)
for i in p:
    print(i, end=' ')


