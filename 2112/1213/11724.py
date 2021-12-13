import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())
node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    x,y = map(int,input().split())
    node[x].append(y)
    node[y].append(x)
que = []
ans = []
for i in range(1,N+1):
    if visited[i] == 0:
        temp = []
        que.append(i)
        visited[i] = 1
        temp.append(i)
    while que:
        a = que.pop()
        for b in node[a]:
            if visited[b] == 0:
                que.append(b)
                temp.append(b)
                visited[b] = 1
    if temp not in ans:
        ans.append(temp)
print(len(ans))
