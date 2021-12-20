import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
def bfs(position, size):
    dq = deque()
    dq.append(position)
    visit[position[0]][position[1]] = 1
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visit[nx][ny] != 0:
                continue
            if space[nx][ny] > size:
                continue
            visit[nx][ny] = visit[x][y] + 1
            dq.append((nx, ny))

def get(now_size):
    x, y = 0, 0
    min_dist = 999999
    for i in range(N):
        for j in range(N):
            if visit[i][j] != 0 and space[i][j] > 0 and space[i][j] < now_size:
                if min_dist > visit[i][j] - 1:
                    min_dist = visit[i][j] - 1
                    x = i
                    y = j
    return (x, y, min_dist)
N = int(input())
dx = [-1,0,0,1]
dy = [0,-1,1,0]

ans = 0
size = 2
ate = 0
position = (0,0)
space = [list(map(int,input().split())) for _ in range(N)]

for a in range(N):
    for b in range(N):
        if space[a][b] == 9:
            position = (a,b)
            space[a][b] = 0

while True:
    visit = [[0] * N for _ in range(N)]
    bfs(position, size)
    x, y, dist = get(size)
    if dist != 999999:
        ans += dist
        position = (x, y)
        ate += 1
        if ate == size:
            size += 1
            ate = 0
        space[x][y] = 0
    else:
        break
print(ans)

