import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
print(max(int(str(A)[::-1]), int(str(B)[::-1])))
