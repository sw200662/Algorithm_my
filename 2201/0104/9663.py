import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
ans = 0
row = [0] * N


def check(a):
    for i in range(a):
        if row[a] == row[i] or abs(row[a] - row[i]) == a-i:
            return False
    return True

def dfs(a):

    global ans

    if a == N:
        ans += 1
    else:
        for i in range(N):
            row[a] = i
            if check(a):
                dfs(a+1)


dfs(0)
print(ans)