def print_it(star, cnt):
    if cnt == int(N**(1/3)):
        return
    for i in range(len(star)):
        # print(''.join(star[i]))
        print_it(star[i], cnt + 1)
        print(star[i])

def print_star(n, star):
    if n == N * 3:
        print(star)
        return
    stars = []
    stars.append(star * 3)
    tmp = ''
    for _ in range(n // 3):
        tmp += ' '
    stars.append(star + [tmp] * (n // 3) + star)
    stars.append(star * 3)
    print_star(n * 3, stars)

N = int(input())
print_star(3, ['*'])
