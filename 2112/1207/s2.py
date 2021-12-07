import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    R,C = map(int,input().split())
    fish = [list(map(int, input().split())) for _ in range(R)]
    answer = 1
    power = 0
    bird = 0
    no = []
    for b in range(R):
        if b > power:
            break
        for a in range(C):
            if fish[b][a] == 2:
                no.append(a)
            if fish[b][a] == 1:
                if a in no:
                    pass
                else:
                    answer += (abs(bird-a) + 1)
                    bird = a
                    power += 1
    print('#{} {}'.format(tc,answer))