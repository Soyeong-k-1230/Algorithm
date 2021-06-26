import sys
sys.stdin = open('../../input.txt', 'r')

alpha = {}
ans = []
word = list(input().upper())

for w in word:
    if w not in alpha.keys():
        alpha[w] = 1
    else:
        alpha[w] += 1

max_v = max(alpha.values())

for key, val in alpha.items():
    if val == max_v:
        ans.append(key)

if len(ans) != 1:
    print('?')
else:
    print(ans[0])

