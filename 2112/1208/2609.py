import sys

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
max = N*M
# ans1 = 0
# ans2 = 0
# if N > M:
#     for i in range(M, 0, -1):
#         if N % i == 0 and M % i == 0:
#             ans1 = i
#             break
#     for a in range(N,(N*M+1)//2 + 1):
#         if a % N == 0 and a % M == 0:
#             ans2 = a
#             break
#         if a == (N*M+1)//2:
#             ans2 = N*M
# else:
#     for i in range(N, 0, -1):
#         if N % i == 0 and M % i == 0:
#             ans1 = i
#             break
#     for a in range(M,(N*M+1)//2 + 1):
#         if a % N == 0 and a % M == 0:
#             ans2 = a
#             break
#         if a == (N*M+1)//2:
#             ans2 = N*M
# print(ans1)
# print(ans2)

while M != 0:
    N = N % M
    N,M = M,N
print(N)
print(max//N)