import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
M = int(input())
now = 100
remote = [i for i in range(10)]
min_answer = abs(N-100)

if M == 0:
    if now == N:
        print(0)
    else:
        print(min(len(str(N)),min_answer))
else:
    breakdown = list(map(int,input().split()))
    for a in breakdown:
        remote.remove(a)
    for channel in range(1000000):
        for j in range(len(str(channel))):
            if int(str(channel)[j]) not in remote:
                break
            elif len(str(channel)) - 1 == j:
                if min_answer > abs(channel-N) + len(str(channel)):
                    min_answer = abs(channel-N) + len(str(channel))
    print(min_answer)