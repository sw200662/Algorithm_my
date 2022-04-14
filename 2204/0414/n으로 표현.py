N = 5
number = 12


def solution(N, number):
    dp = [[]]
    for i in range(1,9):
        check = []
        for j in range(1,i):
            for a in dp[j]:
                for b in dp[i-j]:
                    check.append(a+b)
                    check.append(a-b)
                    check.append(a*b)
                    if b != 0:
                        check.append(a//b)
        check.append(int(str(N)*i))
        if number in check:
            return i
        dp.append(list(set(check)))
    return -1
solution(N, number)