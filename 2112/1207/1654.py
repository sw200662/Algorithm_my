import sys

sys.stdin = open('input.txt')

K, N = map(int,input().split())
junson = []
for _ in range(K):
    junson.append(int(input()))
start = 1
end = max(junson)

while start <= end:
    temp = 0
    mid = (start + end) // 2
    for i in junson:
        temp += i//mid
    if temp >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)