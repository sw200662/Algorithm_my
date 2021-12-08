import sys
sys.stdin = open('input.txt')

N = int(input())
sang = list(map(int,sys.stdin.readline().split()))
M = int(input())
find = list(map(int,sys.stdin.readline().split()))

count_dict = dict()

for i in sang:
    if i in count_dict:
        count_dict[i] +=1
    else:
        count_dict[i] = 1

for a in range(M):
    if find[a] in count_dict:
        print(count_dict[find[a]], end=' ')
    else:
        print(0, end=' ')