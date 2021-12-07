import sys

sys.stdin = open('input.txt')

T = int(input())

def bfs():

for tc in range(1,T+1):
    R,C = map(int,input().split())
    fish = [list(map(int, input().split())) for _ in range(R)]
    answer = 1
    power = 0
    bird = 0
    no = []