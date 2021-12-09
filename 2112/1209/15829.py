import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

L = int(input())

answer = 0
a = str(input())
for i in range(L):
    b = a[i]
    answer += (ord(b) - 96) * (31 ** i)
print(answer % 1234567891)