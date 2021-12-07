import sys

sys.stdin = open('input.txt')

n = int(input())

some = 666
temp = 0
while True:
    if "666" in str(some):
        temp += 1
    if temp == n:
        break
    some += 1

print(some)