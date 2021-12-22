import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a,b,c = map(int, sys.stdin.readline().split())


def go(a, n):
    if n == 1:
        return a % c
    else:
        temp = go(a, n // 2)
        if n % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c


print(go(a, b))