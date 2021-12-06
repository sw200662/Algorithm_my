import sys
sys.stdin = open('input.txt')

T = int(input())

a = input()
answer = 0
for b in a:
    answer += int(b)
print(answer)