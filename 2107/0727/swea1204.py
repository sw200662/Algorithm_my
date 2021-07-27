T = int(input())

for Test in range(T):
    A = int(input())
    arr = list(map(int,input().split()))
    People = [0]*101
    ans = 0
    a = 0
    count = 0
    for Score in arr:
        for i in range(101):
            if i == Score:
                People[i] += 1
    for k in People:
        if a <= k:
            ans = count
            a = k
        count += 1
    print(f'#{Test+1} {ans}')