import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
num = []
for i in range(N):
    num.append(list(map(int, input().split())))

for a in range(1, N):
    num[a][0] += min(num[a - 1][1], num[a - 1][2])
    num[a][1] += min(num[a - 1][0], num[a - 1][2])
    num[a][2] += min(num[a - 1][1], num[a - 1][0])

print(min(num[N - 1]))
