import sys
sys.stdin = open('input.txt')

N = list(map(int,input().split()))

answer = 0

for a in N:
    answer += a*a
print(answer%10)