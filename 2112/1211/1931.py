import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
num = [[0]*2 for _ in range(N)]

for i in range(N):
    start, end = map(int,input().split())
    num[i][0] = start
    num[i][1] = end

num.sort(key=lambda x:(x[1],x[0]))
ans = 1
end = num[0][1]
for i in range(1,N):
    if num[i][0] >= end:
        ans += 1
        end = num[i][1]

print(ans)