import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
ans = 0
for n in range(1,N+1):
    if n % 5 == 0:
        while n % 5 == 0:
            n = n // 5
            ans += 1

print(ans)