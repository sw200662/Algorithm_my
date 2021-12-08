import sys

sys.stdin = open('input.txt')

T = int(input())

a = list(map(int,input().split()))

cnt = 0
for i in a:
    check = 0
    if i > 1:
        for b in range(2,i):
            if i % b == 0:
                check = 1
                break
        if check == 0:
            cnt += 1
print(cnt)