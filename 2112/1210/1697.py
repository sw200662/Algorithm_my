import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

N, K = map(int,input().split())

# que = deque()
# que.append([N,0])
# max_num = 100000
# while True:
#     que_list = que.popleft()
#     num = que_list[0]
#     distance = que_list[1]
#     if num == K:
#         break
#     for a in (num-1,num+1,num*2):
#         if 0 <= a <= max_num:
#             que.append([a,distance+1])
# print(distance)

que = deque([N])
max_num = 100000
visited = [0] * (max_num+1)

while que:
    a = que.popleft()
    if a == K:
        break

    for i in (a-1,a+1,a*2):
        if 0 <= i <= max_num and not visited[i]:
            visited[i] = visited[a] + 1
            que.append(i)
print(visited[K])