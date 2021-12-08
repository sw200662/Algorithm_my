import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    answer = 0
    H, W, N = map(int, input().split())
    Num = N // H
    room = N % H
    if room == 0:
        room = H * 100
    else:
        room *= 100
        Num = 1 + N // H
    print(room + Num)

# t = int(input())
# for i in range(t):
#     h, w, n = map(int, input().split())
#     f = 0
#     ho = 0
#     if n % h == 0:
#         f = h * 100
#         ho = n // h
#     else:
#         f = (n % h) * 100
#         ho = 1 + n // h
#     print(f + ho)