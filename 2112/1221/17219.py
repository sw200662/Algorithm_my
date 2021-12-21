import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
pw = {}
for i in range(N):
    a,b = map(str,input().split())
    pw[a] = b
for c in range(M):
    d = input().rstrip()
    print(pw[d])