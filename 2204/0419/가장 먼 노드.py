n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
from collections import deque
def solution(n, edge):
    check = [0] * (n+1)
    check[0], check[1] = 1,1
    graph = [[] for _ in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    go = deque()
    for i in graph[1]:
        go.append([i,1])
        check[i] = 1
    while go:
        a,b = go.popleft()
        for i in graph[a]:
            if check[i] == 0:
                go.append([i,b+1])
                check[i] = b+1
    high = max(check)

    return check.count(high)

solution(n, edge)