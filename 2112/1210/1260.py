import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (N + 1)
visited2 = [0] * (N + 1)
que = deque()
que.append(V)
for a in range(len(graph)):
    graph[a].sort()


def dfs(v):
    visited2[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if visited2[i] == 0:
            dfs(i)

dfs(V)
print()
while len(que) != 0:
    i = que.popleft()
    visited[i] = 1
    go = graph[i]
    for a in go:
        if visited[a] == 0:
            que.append(a)
            visited[a] = 1
    print(i, end=' ')
