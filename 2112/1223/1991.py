import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

def first(a):
    if a != '.':
        print(a, end='')
        first(tree[a][0])
        first(tree[a][1])

def second(a):
    if a != '.':
        second(tree[a][0])
        print(a, end='')
        second(tree[a][1])

def third(a):
    if a != '.':
        third(tree[a][0])
        third(tree[a][1])
        print(a, end='')

N = int(input())

tree = {}
for i in range(N):
    x,y,z = map(str,input().split())
    tree[x] = [y,z]
first('A')
print()
second('A')
print()
third('A')