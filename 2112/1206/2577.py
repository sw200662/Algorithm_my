import sys
sys.stdin = open('input.txt')

A = int(input())
B = int(input())
C = int(input())

D = A*B*C
D = str(D)

num_list = [0] * 10
for a in D:
    num_list[int(a)] += 1
for b in range(10):
    print(num_list[b])