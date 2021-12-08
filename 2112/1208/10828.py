import sys

sys.stdin = open('input.txt')

N = int(input())


def push(b, num):
    b.append(num)


def pop(b):
    if len(b) == 0:
        return -1
    else:
        c = b.pop()
        return c


def size(b):
    return len(b)


def empty(b):
    if len(b) == 0:
        return 1
    else:
        return 0

def top(b):
    if len(b) == 0:
        return -1
    else:
        return b[-1]

a = []
for _ in range(N):
    temp = list(map(str, sys.stdin.readline().split()))
    if len(temp) == 2:
        order, M = temp[0], temp[1]
        M = int(M)
    else:
        order = temp[0]


    if order == 'push':
        push(a, M)
    elif order == 'pop':
        print(pop(a))
    elif order == 'size':
        print(size(a))
    elif order == 'empty':
        print(empty(a))
    else:
        print(top(a))
