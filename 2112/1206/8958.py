import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    a = str(input())
    answer = 0
    stack = 0
    for b in a:
        if b == 'X':
            stack = 0
        else:
            stack += 1
            answer += stack
    print(answer)