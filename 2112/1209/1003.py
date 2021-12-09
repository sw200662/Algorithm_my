import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
fibo = [[0,0] for _ in range(41)]
fibo[0][0] = 1
fibo[1][1] = 1
for _ in range(N):
    cnt = 1
    num = int(input())
    if num == 0:
        print(*fibo[0])
    elif num == 1:
        print(*fibo[1])
    else:
        while cnt != num:
           cnt += 1
           fibo[cnt] = [fibo[cnt-2][0] + fibo[cnt-1][0],fibo[cnt-2][1] + fibo[cnt-1][1]]
        print(*fibo[cnt])