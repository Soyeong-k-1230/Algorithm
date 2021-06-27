N, K = map(int, input().split())
ans = []
people = list(map(int, range(1, N + 1)))

while len(ans) != N:
    num = K % len(people)
    ans.append(people[num - 1])
    idx = people.index(people[num - 1])
    people = people[idx + 1:] + people[0:idx]

print('<', end='')
for i in range(len(ans)):
    if i == len(ans) - 1:
        print(ans[i], end='')
    else:
        print(ans[i], end=', ')
print('>')
