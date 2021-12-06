import sys
sys.stdin = open('input.txt')

a,b = map(int,input().split())

a = str(a)
a = a[::-1]
b = str(b)
b = b[::-1]
a = int(a)
b = int(b)
if a > b:
    print(a)
else:
    print(b)