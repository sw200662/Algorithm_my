import sys
sys.stdin = open('input.txt')

N, M = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))
start = 1
end = max(tree)


while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in tree:
        if i - mid > 0:
            temp += i - mid
    if temp >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)