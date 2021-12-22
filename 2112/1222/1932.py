import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

num = [list(map(int,input().split())) for _ in range(n)]
for a in range(1,n):
    for b in range(len(num[a])):
        if b == 0:
            num[a][b] += num[a-1][b]
        elif a == b:
            num[a][b] += num[a-1][b-1]
        else:
            num[a][b] += max(num[a-1][b],num[a-1][b-1])
print(max(num[n-1]))