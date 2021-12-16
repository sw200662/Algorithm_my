import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())

num = list(map(int,input().split()))
sum = [0] * (N+1)
sum[1] = num[0]
for a in range(2,N+1):
    sum[a] = sum[a-1] + num[a-1]
for i in range(M):
    answer = 0
    a,b = map(int,input().split())
    print(sum[b]-sum[a-1])