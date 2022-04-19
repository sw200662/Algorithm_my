numbers = "011"
from itertools import permutations

def find(a):
    b = int(a ** 0.5)
    if a < 2:
        return False

    for i in range(2,b+1):
        if a % i == 0:
            return False

    return True

def solution(numbers):
    answer = []
    # check = [n for n in numbers]
    for i in range(1,len(numbers)+1):
        num_list = list(map(''.join,permutations(numbers,i)))
        for i in num_list:
            i = int(i)
            if find(i) == True:
                answer.append(i)
    return len(set(answer))

solution(numbers)