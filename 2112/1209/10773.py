import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline
K = int(input())
answer = 0
que = deque()
for i in range(K):
    a = int(input())
    if a == 0:
        que.pop()
    else:
        que.append(a)
print(sum(que))

