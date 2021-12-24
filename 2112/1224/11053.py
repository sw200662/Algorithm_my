import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

A = int(input())
num = list(map(int,input().split()))
ans = [1] * A
for i in range(1,A):
    for j in range(i):
        if num[j] < num[i]:
            ans[i] = max(ans[i], ans[j] + 1)
print(max(ans))

