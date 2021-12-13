import sys
sys.stdin = open('input.txt')
import heapq
input = sys.stdin.readline

N = int(input())
que = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(que,-x)
    else:
        if que:
            print(-heapq.heappop(que))
        else:
            print(0)
