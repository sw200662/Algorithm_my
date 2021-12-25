import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
ans = []


def dfs(start):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(start, N + 1):
        ans.append(i)
        dfs(i + 1)
        ans.pop()


dfs(1)
