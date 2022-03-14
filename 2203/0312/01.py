## 최소의 동전합으로 제출하기
money = 4578
costs = [1, 4, 99, 35, 50, 1000]
dong = [1,5,10,50,100,500]

costs2 = []
costs2 = costs[::]
for i in range(len(costs2)):
    costs2[i] = costs2[i] / dong[i]

visit = [0] * 6
answer = 0
while money != 0:
    a = 0
    min_n = 10000000
    for i in range(len(costs2)):
        if costs2[i] < min_n and visit[i] == 0:
            a = i
            min_n = costs2[i]
    visit[a] = i
    answer += money // dong[a] * costs[a]
    money = money % dong[a]



print(visit)
print(costs2)
print(answer)