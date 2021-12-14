import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline



T = int(input())

for i in range(T):
    n = int(input())
    dp = [0] * 6
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    if n > 5:
        dp = [0] * (n + 2)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        for a in range(6,n+1):
            dp[a] = dp[a-1] + dp[a-5]
    print(dp[n])