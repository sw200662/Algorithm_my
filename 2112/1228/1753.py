import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dij(start):
    dis[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        dist, now = heapq.heappop(heap)

        if dis[now] < dist:
            continue

        for i in road[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))

V, E = map(int,input().split())
K = int(input())
road = [[] for _ in range(V+1)]
heap = []

for i in range(E):
    u,v,w = map(int,input().split())
    road[u].append((v,w))

dis = [987654321] * (V + 1)
dij(K)
for i in range(1,len(dis)):
    if dis[i] == 987654321:
        print('INF')
    else:
        print(dis[i])

