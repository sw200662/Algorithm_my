import sys
from collections import Counter
sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())

first = []
second = []

for _ in range(N):
    first.append(input().rstrip())
for _ in range(M):
    second.append(input().rstrip())

found = Counter(second)
answer = []
answer2 = 0
for i in range(N):
    if found[first[i]] == 1:
        answer2 += 1
        answer.append(first[i])
print(answer2)
answer.sort()
for a in answer:
    print(a)
