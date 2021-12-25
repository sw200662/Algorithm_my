import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())
num = [list(map(int,input().split())) for _ in range(N)]

for a in range(N):
    for b in range(N):
        if b == 0:
            pass
        else:
            num[a][b] += num[a][b-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    answer = 0
    for i in range(x1-1,x2):
        if y1 != 1:
            answer -= num[i][y1-2]
        answer += num[i][y2-1]
    print(answer)