import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    check = 0
    go = str(input().rstrip())
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()
    flag = 0

    for a in go:
        if a == 'R':
            if flag == 0:
                flag = 1
            else:
                flag = 0
        elif a == 'D':
            if len(arr) == 0:
                check = 1
                print("error")
                break
            else:
                if flag == 1:
                    arr.pop()
                else:
                    arr.popleft()

    if check == 0:
        if flag == 1:
            arr.reverse()
        print('[' + ','.join(arr) + ']')
