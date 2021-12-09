import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    x, y = map(int, input().split())
    array.append([x, y])
array = sorted(array, key=lambda x: (x[1], x[0]))
for a in array:
    print(*a)