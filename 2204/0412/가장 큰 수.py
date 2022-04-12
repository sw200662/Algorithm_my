numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    temp = list(map(str,numbers))
    temp.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(temp)))
    return answer

solution(numbers)