import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    while que:
        c = que.pop()
        for i in range(4):
            newx = int(c[0]) + dx[i]
            newy = int(c[1]) + dy[i]
            if 0 <= newx < N and 0 <= newy < N and visit[newx][newy] == 0 and home[newx][newy] == '1':
                que.append([newx,newy])
                que1.append([newx,newy])
                visit[newx][newy] = 1

N = int(input())

home = [list(input().rstrip()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
answer = deque()
for a in range(N):
    for b in range(N):
        if home[a][b] == '1' and visit[a][b] == 0:
            que = deque()
            que.append([a,b])
            que1 = deque()
            visit[a][b] = 1
            bfs(a,b)
            answer.append(que1)
real_answer = []
for i in answer:
    real_answer.append(len(i))
real_answer.sort()
print(len(real_answer))
for q in real_answer:
    print(q+1)
