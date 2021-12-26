import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
ans = []
ans2 = set()
num.sort()
check = [0] * N
dic = {}

def dfs(a):
    if len(ans) == M:
        s = ' '.join(map(str, ans))
        if s not in dic:
            dic[s] = 1
            print(s)
        return
    for i in range(N):
        if i >= a:
            ans.append(num[i])
            dfs(i)
            ans.pop()

dfs(0)