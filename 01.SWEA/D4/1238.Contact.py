import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def bfs(v):
    queue = deque()
    queue.append(v)
    visited = [False] * 101
    D = [0] * 101
    visited[v] = True
    while queue:
        n = queue.popleft()
        for w in G[n]:
            if not visited[w]:
                D[w] = D[n] + 1
                visited[w] = True
                queue.append(w)
    return D

for tc in range(1, 11):
    N, S = map(int, input().split())
    contact = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    max_v = -1
    for i in range(0, N, 2):
        G[contact[i]].append(contact[i + 1])
    D = bfs(S)
    max_d = max(D)
    for i in range(101):
        if D[i] == max_d:
            max_v = max(i, max_v)
    print('#{} {}'.format(tc, max_v))
