import sys

sys.stdin = open('input.txt')

M, N = map(int, input().split())

for tc in range(M, N + 1):
    answer = 0
    for i in range(2, int(tc**0.5)+1):
        if tc % i == 0:
            answer = 1
            break
    if answer == 0:
        print(tc)
