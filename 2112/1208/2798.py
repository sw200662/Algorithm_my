import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, M = map(int,input().split())
number = list(map(int,input().split()))
ans = 0
combi = list(combinations(number,3))
for i in range(len(combi)):
    combi[i] = sum(combi[i])
for i in combi:
    if ans < i <= M:
        ans = i
print(ans)