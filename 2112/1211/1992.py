import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
file = [list(input().rstrip()) for _ in range(N)]