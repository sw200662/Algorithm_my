import sys
sys.stdin = open('input.txt')

N = int(input())

check = 0

a = N // 5
b = N % 5
c = b // 3
d = b % 3
check = 0
while d != 0:
    if check == 6:
        break
    check += 1
    a -= 1
    b += 5
    c = b // 3
    d = b % 3
if check == 6 or a < 0:
    print(-1)
else:
    print(a+c)