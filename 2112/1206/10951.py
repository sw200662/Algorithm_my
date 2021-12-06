import sys
sys.stdin = open('input.txt')

while True:
    try:
        a, b = map(int,input().split())
        print(a+b)
    except:
        break