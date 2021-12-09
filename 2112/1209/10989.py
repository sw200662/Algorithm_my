import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
array = [0] * 10001

for _ in range(N):
    a = int(input())
    array[a] += 1

for i in range(10001):
    if array[i] != 0:
        for a in range(array[i]):
            print(i)
