import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import Counter

T = int(input())

for i in range(T):
    n = int(input())
    cloth = []
    for j in range(n):
        a,b = input().split()
        cloth.append(b)
    answer = 1
    cnt = Counter(cloth)
    for c in cnt:
        answer *= cnt[c] + 1
    print(answer-1)