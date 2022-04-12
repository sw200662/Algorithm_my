prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        temp = 0
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                break

            temp += 1

        answer[i] = temp
    answer = []
    return answer

solution(prices)