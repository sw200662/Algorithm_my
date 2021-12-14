import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
word = str(input().rstrip())
que = deque()
cnt = 0
answer = 0
for i in range(len(word)):
    if word[i] == 'I':
        que.append(i)


for i in range(1,len(que)):
    if que[i] - que[i-1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= N:
        answer += 1
print(answer)