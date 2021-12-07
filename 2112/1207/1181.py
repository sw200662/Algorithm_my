import sys

sys.stdin = open('input.txt')

N = int(input())

answer = []

for _ in range(N):
    word = input()

    if (len(word), word) not in answer:
        answer.append((len(word),word))

answer = sorted(answer, key=lambda x: (x[0], x[1]))

for a in answer:
    print(a[1])
# for _ in range(N):
#     answer.append(str(input()))
# for j in range(0,len(answer)-1):
#     for i in range(len(answer)-j-1):
#         if len(answer[i]) > len(answer[i+1]):
#             answer[i+1], answer[i] = answer[i], answer[i+1]
#         elif len(answer[i]) == len(answer[i+1]):
#             for a in range(len(answer[i])):
#                 if ord(answer[i][a]) > ord(answer[i+1][a]):
#                     answer[i + 1], answer[i] = answer[i], answer[i + 1]
#                     break
# print(answer[0])
# for c in range(1,len(answer)):
#     if answer[c] != answer[c-1]:
#         print(answer[c])

