import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
T = int(input())

for i in range(T):
    A,B = map(int,input().split())
    que = deque()
    que.append([A,''])
    visited = set()
    while que:
        a = que.popleft()
        if a[0] == B:
            print(a[1])
            break
        else:
            if a[0]*2%10000 not in visited:
                que.append([a[0]*2%10000,a[1] + 'D'])
                visited.add(a[0]*2%10000)
            if a[0] == 0 and 9999 not in visited:
                que.append([9999, a[1] + 'S'])
            elif a[0]-1 not in visited:
                que.append([a[0] - 1, a[1] + 'S'])
                visited.add(a[0]-1)
            c = a[0] % 1000 * 10 + a[0] // 1000
            d = a[0] % 10 * 1000 + a[0] // 10
            if c not in visited:
                que.append([c,a[1] + 'L'])
                visited.add(c)
            if d not in visited:
                que.append([d,a[1] + 'R'])
                visited.add(d)
