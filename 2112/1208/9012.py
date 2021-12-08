import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    gual = str(input())
    check = []
    answer = 0
    for a in gual:
        if a == '(':
            check.append(a)
        elif a == ')':
            if len(check) == 0 or check[-1] == ')':
                answer = 1
                break
            else:
                check.pop()
    if len(check) != 0 or answer == 1:
        print('NO')
    else:
        print('YES')
