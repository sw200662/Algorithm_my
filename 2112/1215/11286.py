import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
import heapq
N = int(input())
que = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if len(que) == 0:
            print(0)
        else:
            print(heapq.heappop(que)[1])
    else:
        if a > 0:
            heapq.heappush(que,[abs(a),a])
        else:
            heapq.heappush(que,[abs(a),a])