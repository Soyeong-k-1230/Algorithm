import sys
sys.stdin = open('input.txt', 'r')

L, C = map(int, input().split())
words = list(input().split())
words.sort()
visited = [False] * C

def check(words):
    a = ['a', 'e', 'i', 'o', 'u']
    cnt_a = 0
    cnt_b = 0
    for word in words:
        if word in a:
            cnt_a += 1
        else:
            cnt_b += 1
    if cnt_a > 0 and cnt_b > 1:
        return True
    else:
        return False

def backtrack(n, s, p):
    if n == L:
        if check(p):
            print(p)
        return
    for i in range(s, C):
        if not visited[i]:
            visited[i] = True
            backtrack(n + 1, i, p + words[i])
            visited[i] = False

backtrack(0, 0, '')
