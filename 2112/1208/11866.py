import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())

number = list(i+1 for i in range(N))
pointer = K-1
answer = []
while len(number) != 0:
    if pointer >= len(number):
        pointer -= len(number)
    answer.append(number[pointer])
    number.remove(number[pointer])
    pointer += K-1
    print(answer)