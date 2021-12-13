import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tomato = [list(map(int,input().split())) for _ in range(M)]
que = deque()
for a in range(N):
    for b in range(M):
        if tomato[b][a] == 1:
            que.append([a,b])
while que:
    a = que.popleft()

    for i in range(4):
        new_x = a[0] + dx[i]
        new_y = a[1] + dy[i]
        if 0 <= new_x < N and 0 <= new_y < M and tomato[new_y][new_x] == 0:
            que.append([new_x,new_y])
            tomato[new_y][new_x] = tomato[a[1]][a[0]] + 1
answer = 0
for a in range(N):
    for b in range(M):
        if answer < tomato[b][a]:
            answer = tomato[b][a]
        elif tomato[b][a] == 0:
            print(-1)
            exit(0)
print(answer-1)