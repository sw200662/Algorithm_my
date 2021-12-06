import sys
sys.stdin = open('input.txt')
a = str(input())

for b in range(97,123):
    answer = -1
    for c in range(len(a)):
        if a[c] == chr(b):
            print(c,end=' ')
            answer = c
            break
    if answer == -1:
        print(answer,end=' ')