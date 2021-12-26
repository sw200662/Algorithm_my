import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
ans = []
num.sort()
def dfs(start):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(N):
        if i >= start:
            ans.append(num[i])
            dfs(i)
            ans.pop()

dfs(0)