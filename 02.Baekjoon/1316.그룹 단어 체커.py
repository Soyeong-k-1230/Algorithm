import sys
sys.stdin = open('input.txt', 'r')
ans = 0
for tc in range(int(input())):
    words = list(input())
    group = []
    flag = True
    for i in range(len(words)):
        if i + 1 == len(words):
            if words[i] not in group:
                group.append(words[i])
            else:
                flag = False
            break

        if words[i] != words[i + 1]:
            if words[i] not in group:
                group.append(words[i])
            else:
                flag = False
                break
    if flag:
        ans += 1
print(ans)

