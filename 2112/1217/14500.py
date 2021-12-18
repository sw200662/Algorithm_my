import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

tetrominos = [([0, 0], [0, 1], [0, 2], [0, 3]),
              ([0, 0], [1, 0], [2, 0], [3, 0]),
              ([0, 0], [0, 1], [1, 1], [1, 0]),
              ([0, 0], [1, 0], [1, 1], [1, 2]),
              ([0, 0], [0, 1], [1, 0], [2, 0]),
              ([0, 0], [0, 1], [0, 2], [1, 2]),
              ([0, 1], [1, 1], [2, 1], [2, 0]),
              ([0, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 2]),
              ([0, 0], [1, 0], [2, 0], [2, 1]),
              ([0, 0], [1, 0], [0, 1], [0, 2]),
              ([0, 0], [1, 0], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [0, 1], [0, 2]),
              ([2, 0], [1, 0], [1, 1], [0, 1]),
              ([0, 0], [0, 1], [1, 1], [1, 2]),
              ([0, 0], [0, 1], [1, 1], [0, 2]),
              ([1, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 1]),
              ([0, 0], [1, 0], [1, 1], [2, 0])]

def cal(x,y,te):
    temp = 0
    for i in range(4):
        new_x = x + te[i][0]
        new_y = y + te[i][1]
        if 0 <= new_x < M and 0 <= new_y < N:
            temp += map[new_y][new_x]
        else:
            return 0
    return temp

N,M = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for y in range(N):
    for x in range(M):
        for tet in tetrominos:
            ans = max(ans, cal(x,y,tet))
print(ans)