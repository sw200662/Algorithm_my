import sys

sys.stdin = open('input.txt')
import heapq

input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    num_min = []
    num_max = []
    visited = [False] * k
    for j in range(k):
        x, y = input().split()
        y = int(y)

        if x == 'I':
            heapq.heappush(num_min, (y, j))
            heapq.heappush(num_max, (-y, j))
            visited[j] = True
        elif x == 'D':
            if y == 1:
                while num_max and not visited[num_max[0][1]]:
                    heapq.heappop(num_max)
                if num_max:
                    visited[num_max[0][1]] = False
                    heapq.heappop(num_max)
            else:
                while num_min and not visited[num_min[0][1]]:
                    heapq.heappop(num_min)
                if num_min:
                    visited[num_min[0][1]] = False
                    heapq.heappop(num_min)


    while num_max and not visited[num_max[0][1]]:
        heapq.heappop(num_max)
    while num_min and not visited[num_min[0][1]]:
        heapq.heappop(num_min)

    if not num_max or not num_min:
        print('EMPTY')
    else:
        print(-num_max[0][0], num_min[0][0])
