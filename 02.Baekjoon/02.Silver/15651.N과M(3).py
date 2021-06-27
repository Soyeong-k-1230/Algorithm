N, M = map(int, input().split())

def backtrack(n, s):
    if n == M:
        for num in p:
            print(num, end=" ")
        print()
        return
    for i in range(N):
        if i >= s:
            p[n] = i + 1
            backtrack(n + 1, i)
p = [0] * M
backtrack(0, 0)