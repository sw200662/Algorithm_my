import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    print(' '*(T-i-1), end='')
    print('*'*(i+1))