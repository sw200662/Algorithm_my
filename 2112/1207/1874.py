import sys

sys.stdin = open('input.txt')

N = int(input())
answer = []
check = 0
check2 = 0
check3 = 0
answer2 = []
for i in range(1,N+1):
    T = int(input())
    if T > check2:
        while True:
            if check == T:
                break
            check += 1
            answer.append(check)
            answer2.append('+')
            check2 = answer[-1]
    if T == check2:
        answer.pop()
        answer2.append('-')
        if len(answer) == 0:
            check2 = check
        else:
            check2 = answer[-1]
    elif check2 > T:
        check3 = 1
        break

if check3 == 1:
    print('NO')
else:
    for a in range(len(answer2)):
        print(answer2[a])

