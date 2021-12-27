import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(a,b):
    for i, j in tree[a]:
        if b[i] == -1:
            b[i] = b[a] + j
            dfs(i,b)


N = int(input())
tree = [[] for _ in range(N+1)]
ans = 0
for i in range(1,N+1):
    a = list(map(int,input().split()))
    for j in range(1,len(a)-1):
        if j % 2 == 1:
            continue
        else:
            tree[a[0]].append([a[j-1],a[j]])


ans1 = [-1] * (N+1)
ans1[1] = 0
dfs(1,ans1)

a = max(ans1)
b = ans1.index(a)

ans2 = [-1]*(N+1)
ans2[b] = 0
dfs(b,ans2)
print(max(ans2))