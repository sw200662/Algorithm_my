import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def go(x, y, z):
    global ans

    check = file[x][y]
    for a in range(x, x + z):
        for b in range(y, y + z):
            if file[a][b] != check:
                ans += '('
                for c in range(0, 2):
                    for d in range(0, 2):
                        go(x + z // 2 * c, y + z // 2 * d, z//2)
                ans += ')'
                return

    if check == '0':
        ans += '0'
    if check == '1':
        ans += '1'


N = int(input())
file = [list(input().rstrip()) for _ in range(N)]
ans = ''
go(0, 0, N)
print(ans)