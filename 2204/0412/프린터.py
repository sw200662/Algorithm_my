priorities = [2, 1, 3, 2]
location = 2

from collections import deque

def solution(priorities, location):
    que = deque([(v,i) for i,v in enumerate(priorities)])
    answer = 0
    while True:
        a = que.popleft()
        if que and max(que)[0] > a[0]:
            que.append(a)
        else:
            answer += 1
            if a[0] == location:
                break
    return answer

solution(priorities, location)