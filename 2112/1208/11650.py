import sys
sys.stdin = open('input.txt')

N = int(input())
number = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    number.append([x,y])
number.sort(key=lambda x : (x[0], x[1]))
for i in number:
    print(*i)

