import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
answer = [0] * (N+1)

for i in range(2,N+1):
    answer[i] = answer[i-1] + 1
    if i % 3 == 0:
        answer[i] = min(answer[i], answer[i//3] + 1)
    if i % 2 == 0:
        answer[i] = min(answer[i], answer[i//2] + 1)
print(answer[N])