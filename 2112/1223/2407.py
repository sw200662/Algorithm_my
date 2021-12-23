import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 1
for i in range(1, m + 1):
    ans *= n
    n -= 1
    ans = ans // i
print(ans)