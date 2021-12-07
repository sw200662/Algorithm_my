import sys

sys.stdin = open('input.txt')

while True:
    a = input()
    if a == '0':
        break
    if str(a) == str(a[::-1]):
        print('yes')
    else:
        print('no')