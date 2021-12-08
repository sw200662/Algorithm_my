import sys
sys.stdin = open('input.txt')

while True:
    a,b,c = map(int,input().split())
    number = [a,b,c]
    number.sort()
    a , b , c = number[0], number[1], number[2]
    if a == 0 and b == 0 and c == 0:
        break
    elif a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')