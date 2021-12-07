import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

board = [list(map(str, input().split())) for _ in range(N)]
answer = []

for a in range(N - 7):
    for b in range(M-7):
        temp_1 = 0
        temp_2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][0][j] != 'W':
                        temp_1 += 1
                    else:
                        temp_2 += 1
                else:
                    if board[i][0][j] != 'B':
                        temp_1 += 1
                    else:
                        temp_2 += 1
        answer.append(temp_1)
        answer.append(temp_2)
print(min(answer))