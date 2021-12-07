import sys

sys.stdin = open('input.txt')

N = int(input())
num_list = list(map(int,input().split()))
M = int(input())
find_list = list(map(int,input().split()))
num_list.sort()
for i in find_list:
    answer = 0
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] > i:
            end = mid - 1
        elif num_list[mid] < i:
            start = mid + 1
        else:
            answer = 1
            break
    print(answer)