import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
cnt = 1
answer = 1
num = 6

while N > cnt:
    answer += 1
    cnt += num
    num += 6
print(answer)