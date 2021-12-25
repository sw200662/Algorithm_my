import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

Tree = [[] for _ in range(N+1)]
answer = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

def dfs(c):
    for i in Tree[c]:
        if answer[i] == 0:
            answer[i] = c
            dfs(i)
dfs(1)
for a in range(2,N+1):
    print(answer[a])