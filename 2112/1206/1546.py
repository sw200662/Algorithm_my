import sys
sys.stdin = open('input.txt')

N = int(input())

a = list(map(int,input().split()))
answer = 0
max_score = max(a)
for b in a:
    answer += (b*100/max_score)
answer /= N
print(answer)