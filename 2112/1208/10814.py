import sys
sys.stdin = open('input.txt')

N = int(input())
people_list = [[] for _ in range(201)]
for i in range(N):
    N, M = map(str,sys.stdin.readline().split())
    people_list[int(N)].append(M)
for a in range(len(people_list)):
    if len(people_list[a]) > 0:
        for b in people_list[a]:
            print('{} {}'.format(a,b))