import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

value = deque()
day = deque()
purchase = [(input().rstrip()) for _ in range(3)]

print(purchase)

ans = [0] * 5

for i in range(1,366):
    pass