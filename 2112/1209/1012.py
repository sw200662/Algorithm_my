import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find(x, y):
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < M and 0 <= new_y < N and farm[new_y][new_x] == 1:
            farm[new_y][new_x] = 0
            find(new_x,new_y)

for tc in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    answer = 0
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    for a in range(M):
        for b in range(N):
            if farm[b][a] == 1:
                farm[b][a] = 0
                answer += 1
                find(a, b)
    print(answer)
