import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m,B = map(int,input().split())

earth = [list(map(int,input().split())) for _ in range(n)]
answer = 10000000000000
height = 0
min_value = min(map(min,earth))
max_value = max(map(max,earth))

for i in range(min_value,max_value+1):
    up = 0
    down = 0
    for a in range(n):
        for b in range(m):
            dif = earth[a][b] - i

            if dif > 0:
                down += dif
            elif dif < 0:
                up -= dif
    if down+B >= up:
        time = down*2 + up

        if answer >= time:
            answer = time
            height = i

print(answer,height)