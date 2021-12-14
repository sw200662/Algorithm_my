import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M ,H = map(int,input().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
tomato = []
for i in range(H):
    tomato.append([list(map(int,input().split())) for _ in range(M)])
que = deque()
check = 0
for a in range(N):
    for b in range(M):
        for z in range(H):
            if tomato[z][b][a] == 0:
                check = 1

if check != 1:
    print(0)
else:
    for a in range(N):
        for b in range(M):
            for z in range(H):
                if tomato[z][b][a] == 1:
                    que.append([z,a,b])
    while que:
        a = que.popleft()

        for i in range(6):
            new_x = a[1] + dx[i]
            new_y = a[2] + dy[i]
            new_z = a[0] + dz[i]
            if 0 <= new_x < N and 0 <= new_y < M and 0 <= new_z < H and tomato[new_z][new_y][new_x] == 0:
                que.append([new_z,new_x,new_y])
                tomato[new_z][new_y][new_x] = tomato[a[0]][a[2]][a[1]] + 1


    answer = 0
    for a in range(N):
        for b in range(M):
            for z in range(H):
                if answer < tomato[z][b][a]:
                    answer = tomato[z][b][a]
                elif tomato[z][b][a] == 0:
                    print(-1)
                    exit(0)
    print(answer-1)