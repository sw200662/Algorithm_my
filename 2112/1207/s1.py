import sys

sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def go(x, y, n, temp):
    global answer
    if n == 0:
        return
    if answer <= temp:
        return
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < M and visited[new_y][new_x] == 0:
            if mount[new_y][new_x] == 1:
                if n != 1:
                    visited[new_y][new_x] = 1
                    go(new_x, new_y, n - 1, temp)
                visited[new_y][new_x] = 1
                go(new_x, new_y, L, temp + 1)
                visited[new_y][new_x] = 0
            elif mount[new_y][new_x] == 0:
                visited[new_y][new_x] = 1
                go(new_x, new_y, n - 1, temp)
                visited[new_y][new_x] = 0
            elif mount[new_y][new_x] == 3:
                visited[new_y][new_x] = 0
                if temp < answer:
                    answer = temp


T = int(input())
for tc in range(1, T + 1):
    answer = 5000
    M, N, L = map(int, input().split())
    mount = [list(map(int, input().split())) for _ in range(M)]
    choi = []
    choi2 = []
    for a in range(N):
        for b in range(M):
            if mount[b][a] == 1:
                choi.append([a,b])
                choi2.append(N-a+b-1)
    visited = [[0] * N for _ in range(M)]
    visited[M - 1][0] = 1
    if len(choi2) == 0 or min(choi2) <= L:
        go(0, M - 1, L, 0)
    else:
        pass
    if answer == 5000:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, answer))
