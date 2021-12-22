import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A,B,C = map(int,input().split())

check = 2
D = A
while check < B:
    check = check*2
    A *= A
    A %= C

for i in range(B-check//2):
    A *= D
    A %= C

print(A%C)