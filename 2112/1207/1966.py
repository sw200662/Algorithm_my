import sys

sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(1,T+1):
    cnt = 0
    N, M = map(int,input().split())
    printer_deque = deque()
    number = list(map(int,input().split()))
    for i in range(N):
        printer_deque.append([number[i],i+1])
    while True:
