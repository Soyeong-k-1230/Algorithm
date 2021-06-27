import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
P = list(map(int, input().split()))
tmp = []
ans = []

for i in range(N):
    height = P[i]
    if len(tmp) == 0:
        tmp.append(height)
    elif tmp[-1] < height:
        tmp.append(height)
    elif tmp[-1] >= height:
        ans.append(max(tmp) - min(tmp))
        tmp = []
        tmp.append(height)

if len(tmp) != 0:
    ans.append(max(tmp) - min(tmp))

print(max(ans))
