import sys
sys.stdin = open('../../input.txt', 'r')
words = input().strip()
if words != '':
    print(len(words.split(' ')))
else:
    print(0)
# print(input().strip().split(' '))
# print(len(list(input().strip().split(' '))))
