import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
ans = 0
a = len(str(N))
for i in range(N-9*a,N+1):
    if i > 0:
        b = str(i)
        temp_ans = i
        for c in b:
            temp_ans += int(c)
        if temp_ans == N:
            ans = i
            break
print(ans)