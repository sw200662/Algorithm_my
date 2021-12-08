import sys

sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    N, M = map(int, input().split())
    printer_deque = deque()
    number = list(map(int, input().split()))
    check3 = 0
    for_check = M

    for i in range(N):
        printer_deque.append([number[i], i])

    while check3 == 0:
        check = 0
        check2 = 0
        point = printer_deque[0][0]

        for i in printer_deque:
            if point < i[0]:
                check2 = 1

        if check2 == 1:
            printer_deque.rotate(-1)
            check = 1

        if check == 0:
            a = printer_deque.popleft()
            cnt += 1
            if a[1] == for_check:
                check3 = 1
    print(cnt)
