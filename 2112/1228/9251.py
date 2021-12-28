import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a = str(input().rstrip())
b = str(input().rstrip())
l1, l2 = len(a), len(b)
ans = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < ans[j]:
            cnt = ans[j]
        elif a[i] == b[j]:
            ans[j] = cnt + 1

print(max(ans))
