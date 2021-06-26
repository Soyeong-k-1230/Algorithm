import sys
sys.stdin = open('../../input.txt', 'r')

for tc in range(int(input())):
    R, S = input().split()
    for w in S:
        print(w * int(R), end='')
    print()
