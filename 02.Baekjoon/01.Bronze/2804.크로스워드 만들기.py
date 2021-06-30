import sys
sys.stdin = open('input.txt', 'r')

A, B = input().split()
boards = [['.'] * len(A) for _ in range(len(B))]
s = [0, 0]

def find():
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                s[0] = j
                s[1] = i
                return

find()

for c in range(len(A)):
    boards[s[0]][c] = A[c]

for r in range(len(B)):
    boards[r][s[1]] = B[r]


for i in range(len(B)):
    for j in range(len(A)):
        print(boards[i][j], end='')
    print()