req_id = ["Morgan", "Teo", "Covy", "Covy", "Felix"]
req_info = [[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]]

id = set(req_id)
answer = {}
for i in id:
    answer[i] = [0, 0]
id = list(id)
id.sort()
buy = []
buy_price = []
sell = []
sell_price = []

for i in range(len(req_info)):
    if req_info[i][0] == 0:
        buy.append([req_id[i], req_info[i][1]])
        buy_price.append(req_info[i][2])
    else:
        sell.append([req_id[i], req_info[i][1]])
        sell_price.append(req_info[i][2])

while True:
    buy_person = buy[buy_price.index(max(buy_price))]
    sell_person = sell[sell_price.index(min(sell_price))]
    if min(sell_price) <= max(buy_price):
        if sell_price == 0:
            break
        if buy_person[1] > sell_person[1]:
            answer[buy_person[0]][0] += sell_person[1]
            answer[buy_person[0]][1] -= sell_person[1] * min(sell_price)
            answer[sell_person[0]][0] -= sell_person[1]
            answer[sell_person[0]][1] += sell_person[1] * min(sell_price)
            buy_person[1] = buy_person[1] - sell_person[1]
            sell_person[1] = 0
            sell_price[sell_price.index(min(sell_price))] = 999999999999
        elif buy_person[1] < sell_person[1]:
            answer[buy_person[0]][0] += buy_person[1]
            answer[buy_person[0]][1] -= buy_person[1] * min(sell_price)
            answer[sell_person[0]][0] -= buy_person[1]
            answer[sell_person[0]][1] += buy_person[1] * min(sell_price)
            sell_person[1] = sell_person[1] - buy_person[1]
            buy_person[1] = 0
            buy_price[buy_price.index(max(buy_price))] = 0
    else:
        break
real_answer = []
for i in id:
    a,b = answer[i][0],answer[i][1]
    if a > 0:
        a = '+' + str(a)
    elif a <= 0:
        a = str(a)

    if b > 0:
        b = '+' + str(b)
    elif b <= 0:
        b = str(b)
    real_answer.append(i + ' ' + a + ' ' + b)
print(real_answer)

