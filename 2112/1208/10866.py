import sys

sys.stdin = open('input.txt')

N = int(input())

def push_back(b, num):
    b.append(num)

def push_front(b, num):
    b.insert(0,num)

def pop_back(b):
    if len(b) == 0:
        return -1
    else:
        c = b.pop()
        return c

def pop_front(b):
    if len(b) == 0:
        return -1
    else:
        c = b.pop(0)
        return c


def size(b):
    return len(b)

def empty(b):
    if len(b) == 0:
        return 1
    else:
        return 0

def front(b):
    if len(b) == 0:
        return -1
    else:
        return b[0]

def back(b):
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


    if order == 'push_front':
        push_front(a, M)
    elif order == 'push_back':
        push_back(a, M)
    elif order == 'pop_front':
        print(pop_front(a))
    elif order == 'pop_back':
        print(pop_back(a))
    elif order == 'size':
        print(size(a))
    elif order == 'empty':
        print(empty(a))
    elif order == 'front':
        print(front(a))
    else:
        print(back(a))