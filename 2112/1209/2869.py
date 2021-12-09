import sys
sys.stdin = open('input.txt')

A, B, V = map(int,input().split())

if V > A:
    temp = V - A
    cnt = temp // (A-B)
    snail = cnt * (A-B)
else:
    snail = A
    cnt = 1
while snail < V:
    snail += A
    cnt += 1
    if snail >= V:
        break
    snail -= B
print(cnt)