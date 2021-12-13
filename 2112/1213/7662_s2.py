import sys
sys.stdin = open('input.txt')
import heapq

input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    num_min = []
    num_max = []
    min_del = 0
    max_del = 0
    insert = 0
    for j in range(k):
        x, y = input().split()
        y = int(y)

        if x == 'I':
            heapq.heappush(num_min, y)
            heapq.heappush(num_max, -y)
            insert += 1
        elif x == 'D' and insert > min_del + max_del:
            if y == 1:
                heapq.heappop(num_max)
                max_del += 1
            else:
                heapq.heappop(num_min)
                min_del += 1
    if insert <= min_del + max_del:
        print('EMPTY')
    else:
        print(-num_max[0], num_min[0])
