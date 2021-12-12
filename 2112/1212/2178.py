import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

miro = []
for _ in range(N):
    miro.append(list(map(int, input())))


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M and miro[new_x][new_y] == 1:
                miro[new_x][new_y] = miro[x][y] + 1
                queue.append((new_x, new_y))

    return miro[N - 1][M - 1]


print(bfs(0, 0))