import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
ans = []
num = list(map(int,input().split()))
num.sort()

def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(N):
        if num[i] not in ans:
            ans.append(num[i])
            dfs()
            ans.pop()
dfs()
