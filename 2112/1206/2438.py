import sys
sys.stdin = open('input.txt')
a = []
for i in range(9):
    b = int(input())
    a.append(b)

c = max(a)
d = a.index(c)
print(c)
print((d+1))

