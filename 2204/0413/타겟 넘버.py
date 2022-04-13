numbers = [4, 1, 2, 1]
target = 4

def solution(numbers, target):
    answer = [0]
    for i in numbers:
        temp = []
        for a in answer:
            temp.append(a+i)
            temp.append(a-i)
        answer = temp
    answer = answer.count(target)

    return answer


solution(numbers, target)