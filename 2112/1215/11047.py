import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
que = deque()
ans = 0
for _ in range(N):
    que.append(int(input()))
while K != 0:
    a = que.pop()
    ans += K // a
    K = K % a
print(ans)