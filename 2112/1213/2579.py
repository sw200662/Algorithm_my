import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

chair = [int(input()) for _ in range(N)]
arr = []

if N >= 3:
    arr.append(chair[0])
    arr.append(max(chair[0]+chair[1],chair[1]))
    arr.append(max(chair[0]+chair[2],chair[1]+chair[2]))
    for i in range(3,N):
        arr.append(max(arr[i-2]+chair[i],arr[i-3] + chair[i-1] + chair[i]))
elif N == 2:
    arr.append(chair[0] + chair[1])
elif N == 1:
    arr.append(chair[0])
else:
    arr.append(0)
print(arr.pop())
