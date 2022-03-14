n = 6
clockwise = False
check = n
answer = [[0] * n for _ in range(n)]
n -= 1

k = 0
c = 1
flag = 0
if clockwise == True:
    start = [[0, 0], [n, 0], [n, n], [0, n]]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while n >= 0:
        for i in range(4):
            f = c
            z = (k+i) % 4
            for a in range(n):
                answer[start[i][1]+dy[z]*a][start[i][0]+dx[z]*a] = f
                f += 1
            start[i] = [start[i][0]+dx[z]*a,start[i][1]+dy[z]*a]
        if flag == 0:
            flag = 1
            n -= 1
        else:
            n -= 2
        c = f -1
        k += 1
else:
    start = [[0, 0], [0, n], [n, n], [n, 0]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while n >= 0:
        for i in range(4):
            f = c
            z = (k + i) % 4
            for a in range(n):
                answer[start[i][1] + dy[z] * a][start[i][0] + dx[z] * a] = f
                f += 1
            start[i] = [start[i][0] + dx[z] * a, start[i][1] + dy[z] * a]
        if flag == 0:
            flag = 1
            n -= 1
        else:
            n -= 2
        c = f - 1
        k += 1

if answer[check//2][check//2] == 0:
    answer[check // 2][check // 2] = c + 1
print(answer)