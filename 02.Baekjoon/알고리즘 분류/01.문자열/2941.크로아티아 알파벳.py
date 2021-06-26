import sys
sys.stdin = open('../../input.txt', 'r')

words = input()
i = 0
ans = 0
while i < len(words):
    if i + 1 == len(words):
        ans += 1
        break
    if words[i] == 'c' and (words[i + 1] == '=' or words[i + 1] == '-'):
        i += 2
        ans += 1
        continue
    if words[i] == 'd':
        if words[i + 1] == '-':
            i += 2
            ans += 1
            continue
        if words[i + 1:i + 3] == 'z=':
            i += 3
            ans += 1
            continue
    if words[i: i + 2] in ['lj', 'nj', 's=', 'z=']:
        i += 2
        ans += 1
        continue
    i += 1
    ans += 1
print(ans)
