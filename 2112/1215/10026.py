import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
map1 = [list(str(input().rstrip())) for _ in range(N)]
map2 = [[] * N for _ in range(N)]
visit = [[0] * N for _ in range(N)]
visit2 = [[0] * N for _ in range(N)]
for a in range(N):
    for b in range(N):
        if map1[a][b] == 'R' or map1[a][b] == 'G':
            map2[a].append('R')
        else:
            map2[a].append('B')
answer = 0
answer2 = 0
que = deque()
que2 = deque()
for a in range(N):
    for b in range(N):
        if visit[a][b] == 0:
            que.append([a,b])
            visit[a][b] = 1
            check = map1[a][b]
            answer += 1
            while que:
                x,y = que.popleft()

                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < N and 0 <= new_y < N and visit[new_x][new_y] == 0:
                        if check == map1[new_x][new_y]:
                            que.append([new_x,new_y])
                            visit[new_x][new_y] = 1
for a in range(N):
    for b in range(N):
        if visit2[a][b] == 0:
            que2.append([a,b])
            visit2[a][b] = 1
            check = map2[a][b]
            answer2 += 1
            while que2:
                x,y = que2.popleft()

                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < N and 0 <= new_y < N and visit2[new_x][new_y] == 0:
                        if check == map2[new_x][new_y]:
                            que2.append([new_x,new_y])
                            visit2[new_x][new_y] = 1

print(answer,answer2)


