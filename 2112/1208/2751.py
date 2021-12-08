import sys

sys.stdin = open('input.txt')

N = int(input())

number = []

for _ in range(N):
    number.append(int(sys.stdin.readline()))
number.sort()
for a in number:
    print(a)