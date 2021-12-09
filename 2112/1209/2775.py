import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    apart = [[] for _ in range(a+1)]
    apart[0] = [i+1 for i in range(b)]
    check = 1
    while check != a + 1:
        temp = []
        for i in range(b):
            temp2 = 0
            for c in range(0,i+1):
                temp2 += apart[check-1][c]
            temp.append(temp2)
        apart[check] = temp
        check += 1
    print(apart[check-1][b-1])
