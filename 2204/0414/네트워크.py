n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
from collections import deque
def solution(n, computers):
    answer = 0
    check = [0] * n
    go = deque([0])
    for i in range(len(computers)):
        if check[i] == 0:
            go.append(i)
            check[i] = 1
            answer += 1
        while go:
            a = go.popleft()
            for b in range(len(computers[a])):
                if computers[a][b] == 1 and check[b] == 0:
                    check[b] = 1
                    go.append(b)
    return answer


solution(n, computers)