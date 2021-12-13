import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def dfs(x, y, z):
    global answer, answer2
    check = paper[x][y]

    for a in range(x,x+z):
        for b in range(y,y+z):
            if paper[a][b] != check:
                for c in range(2):
                    for d in range(2):
                        dfs(x + z // 2 * c, y + z // 2 * d, z//2)
                return
    if check == 0:
        answer += 1
    if check == 1:
        answer2 += 1

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
answer = 0
answer2 = 0
dfs(0,0,N)

print(answer)
print(answer2)