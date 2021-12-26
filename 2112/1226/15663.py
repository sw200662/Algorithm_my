import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))
ans = []
num.sort()
dic = {}
check = [0] * N

def dfs():
    if len(ans) == M:
        s = ' '.join(map(str, ans))
        if s not in dic:
            dic[s] = 1
            print(s)
        return
    for i in range(N):
        if check[i]:
            continue
        ans.append(num[i])
        check[i] = 1
        dfs()
        ans.pop()
        check[i] = 0
dfs()