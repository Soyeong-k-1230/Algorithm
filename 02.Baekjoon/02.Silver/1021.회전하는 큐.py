from collections import deque
import sys
sys.stdin = open('../알고리즘 분류/02.큐/input.txt', 'r')

N, M = map(int, input().split())
order = list(map(int, input().split()))
queue = deque(list(map(int, range(1, N + 1))))
print(queue)