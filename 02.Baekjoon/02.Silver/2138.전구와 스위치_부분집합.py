import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

N = int(input())
st = list(map(int, input()))
ed = list(map(int, input()))
ans = 1e10

def subset(k, p):
    global ans

    if k == N:
        arr = [0] * N
        for j in range(N):
            arr[j] = st[j]
        for n in p:
            if n - 1 >= 0:
                arr[n - 1] = 1 >> arr[n - 1]
            arr[n] = 1 >> arr[n]
            if n + 1 < N:
                arr[n + 1] = 1 >> arr[n + 1]

        if arr == ed:
            ans = min(ans, len(p))

        return

    subset(k + 1, p)
    subset(k + 1, p + [k])

subset(0, [])
if ans != 1e10:
    print(ans)
else:
    print(-1)