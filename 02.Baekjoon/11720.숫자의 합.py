import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
print(sum(list(map(int, list(input())))))