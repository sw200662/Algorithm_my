import sys

sys.stdin = open('input.txt')

T = int(input())


def bfs():
    global axis, cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = exno_list[cnt][0], exno_list[cnt][1]
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if 0 <= new_x < N and 0 <= new_y < N and visit_list[new_x][new_y] == 0 and cnt < len(exno_list)-1:
            axis = k
            visit_list[new_x][new_y] = visit_list[x][y] + 1
            go_end(new_x,new_y)



def go_end(x, y):
    global ans, cnt, check, temp_ans, temp_sum
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    new_x = x + dx[axis]
    new_y = y + dy[axis]

    if 0 <= new_x < N and 0 <= new_y < N and visit_list[new_x][new_y] == 0:
        visit_list[new_x][new_y] = visit_list[x][y] + 1
        go_end(new_x,new_y)
    elif new_x == 0 or new_x == N-1 or new_y == 0 or new_y == N-1:
        temp_ans += 1
        cnt += 1
        temp_sum += visit_list[x][y] - 1
        return
    else:
        visit_list[x][y] = 0
        return

for tc in range(1, T + 1):
    N = int(input())
    ex_list = [list(map(int, input().split())) for _ in range(N)]
    visit_list = ex_list[:]
    cnt = 0
    ans = 10000
    temp_ans = 0
    axis = 0
    check = 0
    temp_sum = 0
    exno_list = []
    for a in range(1, N - 1):
        for b in range(1, N - 1):
            if ex_list[a][b] == 1:
                exno_list.append([a, b])
    bfs()
    print(temp_sum)
