import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
que = deque()

A, B = map(int,input().split())

que.append([A,1])
check = 0
while que:
    a = que.popleft()
    if a[0] > B:
        pass
    elif a[0] == B:
        print(a[1])
        check = 1
    else:
        que.append([a[0]*2,a[1]+1])
        c = str(a[0]) + str(1)
        c = int(c)
        que.append([c,a[1]+1])

if check == 0:
    print(-1)