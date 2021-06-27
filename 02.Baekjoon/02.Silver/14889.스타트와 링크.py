import sys
sys.stdin = open('input.txt', 'r')

def total(arr):
    result = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            result += (skill[arr[i]][arr[j]] + skill[arr[j]][arr[i]])
    return result

def dfs(n, p, s):
    global minV
    if n == N // 2:
        a = []; b = []
        for i in range(N):
            if p[i]:
                a.append(i)
            else:
                b.append(i)
        minV = min(minV, abs(total(a) - total(b)))
        return
    for i in range(s, N):
        if not p[i]:
            p[i] = 1
            dfs(n + 1, p, i + 1)
            p[i] = 0

N = int(input())
skill = [list(map(int, input().split())) for _ in range(N)]
p = [0] * N
minV = 1e10
dfs(0, p, 0)
print(minV)