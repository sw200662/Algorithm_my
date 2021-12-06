import sys
sys.stdin = open('input.txt')

a = list(map(int,input().split()))
answer = 0
if a[0] == 1:
    for b in range(len(a)):
        if a[b] != b+1:
            answer = 1
    if answer == 0:
        print('ascending')
    else:
        print('mixed')

elif a[0] == 8:
    for c in range(len(a)):
        if a[c] != 8 - c:
            answer = 1
    if answer == 0:
        print('descending')
    else:
        print('mixed')
else:
    print('mixed')
