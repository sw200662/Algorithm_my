import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    num1 = list(map(int,input().split()))
    num2 = list(map(int, input().split()))
    num1[1] += num2[0]
    num2[1] += num1[0]
    for a in range(2,N):
        num1[a] += max(num2[a-1],num2[a-2])
        num2[a] += max(num1[a-1],num1[a-2])
    print(max(num1[N-1],num2[N-1]))
