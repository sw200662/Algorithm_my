import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x,y,a):
    global answer, answer2, answer3
    check = paper[y][x]
    for i in range(x,x+a):
        for j in range(y,y+a):
            if paper[j][i] != check:
                for c in range(3):
                    for d in range(3):
                        find(x + c*a//3,y + d*a//3, a//3)
                return



    if check == -1:
        answer += 1
    elif check == 0:
        answer2 += 1
    else:
        answer3 += 1


N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
answer = 0
answer2 = 0
answer3 = 0
find(0,0,N)

print(answer)
print(answer2)
print(answer3)