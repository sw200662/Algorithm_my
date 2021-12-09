import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

people = []
for i in range(N):
    X,Y = map(int,input().split())
    people.append([X,Y])
for a in people:
    cnt = 1
    for b in people:
        if a[0] < b[0] and a[1] < b[1]:
            cnt += 1
    print(cnt,end=' ')
