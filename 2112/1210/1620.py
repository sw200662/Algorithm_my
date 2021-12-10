import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())
pokemon = {}
for i in range(1,N+1):
    a = input().rstrip()
    pokemon[i] = a
    pokemon[a] = i
for _ in range(M):
    m = input().rstrip()
    if m.isdigit():
        print(pokemon[int(m)])
    else:
        print(pokemon[m])