array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i in commands:
        temp = [0] * (i[1]-i[0]+1)
        for k in range(i[0]-1,i[1]):
            temp[k-(i[0]-1)] = array[k]
        temp.sort()
        answer.append(temp[i[2]-1])

    return answer

solution(array, commands)