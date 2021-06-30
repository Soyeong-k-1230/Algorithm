import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
cnt = [0] * N

for n in range(N):
    c, g, s, b = map(int, input().split())
    cnt[c - 1] = g + s * (1/1e6) + b * (1/1e12)

country = cnt[K - 1]
bigger = 0

for i in range(N):
    if cnt[i] > country:
        bigger += 1

print(bigger + 1)
