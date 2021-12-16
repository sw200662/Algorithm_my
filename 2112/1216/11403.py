import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for x in range(N):
        for y in range(N):
            if graph[x][k] and graph[k][y]:
                graph[x][y] = 1

for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

