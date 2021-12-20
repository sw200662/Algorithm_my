import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N, M = map(int,input().split())


sadari = [[] for _ in range(101)]
visit = [0 for _ in range(101)]
for _ in range(N):
    x,y = map(int,input().split())
    sadari[x].append(y)
for _ in range(M):
    x,y = map(int,input().split())
    sadari[x].append(y)
que = deque()
que.append([1,0])
visit[1] = 1
check = 0
while True:
    b = que.popleft()
    for i in range(1,7):
        if b[0] + i >= 100:
            check = 1
            break

        if sadari[b[0]+i]:
            a = sadari[b[0]+i][0]
            if visit[a] == 0:
                visit[a] = 1
                que.append([a,b[1]+1])
        elif visit[b[0]+i] == 0:
            visit[b[0]+i] = 1
            que.append([b[0]+i,b[1]+1])
        else:
            pass
    if check == 1:
        break
print(b[1]+1)
