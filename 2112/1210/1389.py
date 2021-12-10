import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


N,M = map(int,input().split())

people = [[] for _ in range(N+1)]
rel = [[0] * (N+1) for _ in range(N+1)]
que = deque()
for _ in range(M):
    x, y = map(int,input().split())
    people[x].append(y)
    people[y].append(x)
for i in range(N+1):
    visited = [0 for _ in range(N + 1)]
    que.append([i,0])
    visited[i] = 1
    while len(que) != 0:
        k = que.popleft()
        b = people[k[0]]
        z = k[1]
        z += 1
        for a in b:
            if visited[a] == 0:
                que.append([a,z])
                visited[a] = 1
                rel[i][a] = z
answer = 9999999
real_ans = 0
for i in range(1,N+1):
    if answer > sum(rel[i]):
        answer = sum(rel[i])
        real_ans = i
print(real_ans)