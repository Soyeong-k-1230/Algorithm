import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
P = list(map(int, input().split()))
max_v = -1


for i in range(N):
    print(P[i])
