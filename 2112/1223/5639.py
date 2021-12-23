import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def go(left,right):
    if left > right:
        return

    div = right + 1
    for i in range(left+1,right+1):
        if tree[left] < tree[i]:
            div = i
            break
    go(left+1, div-1)
    go(div,right)
    print(tree[left])
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

go(0,len(tree)-1)