import sys, heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, X = map(int, input().split())

road = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    road[a].append((b, c))


def dij(start, end):
    dis = [987654321] * (N + 1)
    que = []
    heapq.heappush(que, (0, start))
    dis[start] = 0
    while que:
        dist, now = heapq.heappop(que)

        if dis[now] < dist:
            continue
        for i in road[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

    return dis[end]

result = 0

for i in range(1, N+1):
    first = dij(i,X)
    second = dij(X,i)
    result = max(result, first + second)

print(result)
