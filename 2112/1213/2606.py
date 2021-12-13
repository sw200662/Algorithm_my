import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline


N = int(input())
link = int(input())

computer = [[] for _ in range(N+1)]
for _ in range(link):
    x, y = map(int,input().split())
    computer[x].append(y)
    computer[y].append(x)
que = deque()
que.append(1)
visited = [0 for _ in range(N+1)]
visited[1] = 1
answer = 0
while que:
    a = que.popleft()
    for i in computer[a]:
        if visited[i] == 0:
            que.append(i)
            visited[i] = 1
            answer += 1

print(answer)