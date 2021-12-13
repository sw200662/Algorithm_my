import sys

sys.stdin = open('input.txt')
import heapq

input = sys.stdin.readline

N = int(input())

person = []
time = [0] * (N + 1)
a = list(map(int, input().split()))
for i in a:
    heapq.heappush(person, i)
for b in range(1, N + 1):
    time[b] = time[b-1] + heapq.heappop(person)
print(sum(time))
