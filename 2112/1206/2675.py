import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    a, b = map(str,input().split())
    a = int(a)
    c = len(b)
    for d in range(c):
        print(b[d]*a,end='')
    print()