import sys
sys.stdin = open('input.txt')

while True:
    word = str(sys.stdin.readline().rstrip())
    check = 0
    stack = []
    if word == '.':
        break
    for i in word:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                check = 1
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                check = 1
                break
    if len(stack) != 0:
        check = 1

    if check == 1:
        print('no')
    else:
        print('yes')